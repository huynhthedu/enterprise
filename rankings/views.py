from django.db.models import Sum
from mpl_toolkits.axes_grid1 import make_axes_locatable
from django.http import HttpResponse
import io, os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.use('Agg')

import geopandas as gpd
import fiona
import pandas as pd
import base64, urllib
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Indicator, IndicatorIndex, GroupName
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
# import tkinter as tk
import urllib.parse
import matplotlib.ticker as ticker



def update_label():
    label.config(text="Updated Text")
    root.after(2000, update_label)

    root = tk.Tk()
    label = tk.Label(root, text="Initial Text")
    label.pack()
    root.after(2000, update_label)
    root.mainloop()

def validate_input(request):
    # Fetch available states, indicators, and years
    states = Indicator.objects.values_list('state', flat=True).distinct().order_by('state')
    years = list(range(1999, 2024))

    selected_state = None
    year1 = None
    year2 = None
    warning_message = None
    
    if request.method == 'GET' and 'state' in request.GET and 'year1' in request.GET and 'year2' in request.GET:
        selected_state = request.GET.get('state', '')
        year1 = int(request.GET.get('year1', min(years)))
        year2 = int(request.GET.get('year2', max(years)))
    
        # Validate the year range
        if year2 <= year1:
            warning_message = "Year 2 must be greater than Year 1. Please choose another year."
            return render(request, 'rankings/rankings.html', {
                'states': states,
                'years': years,
                'selected_state': selected_state,
                'year1': year1,
                'year2': year2,
                'warning_message': warning_message,
                'grouped_rankings': None,
                'rankings_data': None,
            })

    return {
        'states': states,
        'years': years,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
    }

def calculate_growth_and_rankings(request):
    validation_result = validate_input(request)
    if isinstance(validation_result, dict):
        states = validation_result['states']
        years = validation_result['years']
        selected_state = validation_result['selected_state']
        year1 = validation_result['year1']
        year2 = validation_result['year2']
        warning_message = validation_result['warning_message']
    else:
        return validation_result  # This will return the rendered response if there's a warning

    filtered_rankings = None  
    growth_data = {}
    rankings_data = []     
    sorted_rankings = None
    grouped_rankings = None

    # Initialize dictionaries for growth and rankings
    all_indicators = Indicator.objects.values_list('indicator', flat=True).distinct()
    all_states = Indicator.objects.values_list('state', flat=True).distinct()

    for indicator in all_indicators:
        state_aggregates_year1 = Indicator.objects.filter(year=year1, indicator=indicator).values('state').annotate(total_value=Sum('value'))
        state_aggregates_year2 = Indicator.objects.filter(year=year2, indicator=indicator).values('state').annotate(total_value=Sum('value'))

        state_map_year1 = {item['state']: item['total_value'] for item in state_aggregates_year1}
        state_map_year2 = {item['state']: item['total_value'] for item in state_aggregates_year2}

        for state in all_states:
            year1_value = state_map_year1.get(state)
            year2_value = state_map_year2.get(state)

            if year1_value is None or year2_value is None:
                continue

            growth = (year2_value - year1_value) / year1_value * 100 if year1_value != 0 else 0
            growth_data[(state, indicator)] = growth

            indicator_details = Indicator.objects.filter(state=state, indicator=indicator).first()
            unit = indicator_details.unit if indicator_details else None
            source = indicator_details.source if indicator_details else None
            group = indicator_details.group if indicator_details else None

            rankings_data.append({
                'state': state,
                'indicator': indicator,
                'year1_value': year1_value,
                'year2_value': year2_value,
                'growth': growth,
                'unit': unit,
                'source': source,
                'group': group,                    
            })

    for indicator in all_indicators:
        indicator_rankings = [data for data in rankings_data if data['indicator'] == indicator]
        year1_rank = sorted(indicator_rankings, key=lambda x: x['year1_value'], reverse=True)
        year2_rank = sorted(indicator_rankings, key=lambda x: x['year2_value'], reverse=True)
        growth_rank = sorted(indicator_rankings, key=lambda x: x['growth'], reverse=True)

        for index, item in enumerate(year1_rank):
            item['year1_rank'] = index + 1
        for index, item in enumerate(year2_rank):
            item['year2_rank'] = index + 1
        for index, item in enumerate(growth_rank):
            item['growth_rank'] = index + 1

    filtered_rankings = [data for data in rankings_data if data['state'] == selected_state]

    sorted_rankings = sorted(filtered_rankings, key=lambda x: x['group'])

    grouped_rankings = {}

    for data in sorted_rankings:
        group_key = data['group'][:2] if data['group'] else 'Other'
        
        # Try to get the group name from the GroupName model
        group_names = GroupName.objects.filter(index=group_key)
        if group_names.exists():
            group_name = group_names.first().name  # Use the first matching object
        else:
            group_name = 'Other'
        
        # Check if the indicator matches any in the IndicatorIndex model
        indicator_exists = IndicatorIndex.objects.filter(indicator=data['indicator']).exists()
        
        if indicator_exists:
            if group_name not in grouped_rankings:
                grouped_rankings[group_name] = []
            grouped_rankings[group_name].append(data)
    
    context = {
        'states': states,
        'years': years,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
        'grouped_rankings': grouped_rankings,
        'rankings_data': sorted_rankings
    }

    return render(request, 'rankings/rankings.html', context)

def indicator_map(request):
    file_path = 'shapefiles/ne_110m_admin_1_states_provinces.shp'
    
    if os.path.exists(file_path):  # Use os.path.exists instead
        with fiona.open(file_path) as src:
            # Do something with the file
            pass
    
    return render(request, 'rankings/indicator_map.html')

def load_shapefile():
    shapefile_path = 'shapefiles/ne_110m_admin_1_states_provinces.shp'
    
    # Check if the shapefile exists
    if not os.path.exists(shapefile_path):
        raise Exception(f"Shapefile not found: {shapefile_path}")

    # Read the shapefile into a GeoDataFrame using geopandas
    gdf = gpd.read_file(shapefile_path)
    return gdf

def select_indicator(request):
    # Fetch available indicators and years
    indicators = Indicator.objects.values_list('indicator', flat=True).distinct()
    years = list(range(1999, 2024))
    
    # Set default selected values
    selected_indicator = request.GET.get('indicator', indicators[0] if indicators else '')
    selected_year = request.GET.get('year', years[-1] if years else '')

    context = {
        'selected_indicator': selected_indicator,
        'selected_year': selected_year,
        'indicators': indicators,
        'years': years,
    }

    return context

def indicator_map(request):
    context = select_indicator(request)
    selected_year = context['selected_year']
    selected_indicator = context['selected_indicator']

    # Fetch data from the database
    indicators = Indicator.objects.filter(indicator=selected_indicator, year=selected_year).values('state', 'value')

    # Prepare data for the map
    indicator_data = {item['state']: item['value'] for item in indicators}

    # Load the US states shapefile from local directory
    us_states = load_shapefile()
    us_states = us_states[us_states['admin'] == 'United States of America']

    # Exclude Alaska and islands
    exclude_states = ['Alaska', 'Hawaii', 'Puerto Rico', 'Guam', 'American Samoa', 'Northern Mariana Islands', 'United States Virgin Islands']
    us_states = us_states[~us_states['name'].isin(exclude_states)]

    # Merge data with the GeoDataFrame
    us_states['indicator_value'] = us_states['name'].map(indicator_data)

    # Add state abbreviations to the GeoDataFrame
    state_abbreviations = {
        'Alabama': 'AL', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
        'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Idaho': 'ID',
        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY',
        'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
        'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
        'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 
        'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
        'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
        'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    us_states['abbr'] = us_states['name'].map(state_abbreviations)

    # Plotting the map
    fig, ax = plt.subplots(1, figsize=(15, 10))
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    us_states.boundary.plot(ax=ax)
    us_states.plot(column='indicator_value', ax=ax, legend=True, cax=cax,
                    legend_kwds={'label': f"{selected_indicator} in {selected_year}",
                                'orientation': "vertical"})

    # Add state abbreviations and values to the map
    for idx, row in us_states.iterrows():
        if row['geometry'].geom_type == 'Polygon':
            x, y = row['geometry'].centroid.x, row['geometry'].centroid.y
        elif row['geometry'].geom_type == 'MultiPolygon':
            x, y = row['geometry'].representative_point().x, row['geometry'].representative_point().y
        else:
            continue

        plt.annotate(text=row['abbr'], xy=(x, y), horizontalalignment='center', fontsize=8, color='black', weight='bold')
        if not pd.isna(row['indicator_value']):
            plt.annotate(text=f"{row['indicator_value']:.1f}", xy=(x, y - 0.5), horizontalalignment='center', fontsize=10, color='blue')

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buf)
    plt.close(fig)

    # Encode the image to base64
    map_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    context['map_image'] = map_image

    return render(request, 'rankings/indicator_map.html', context)



def growth_chart(request):
    indicators = Indicator.objects.values_list('indicator', flat=True).distinct()
    states = Indicator.objects.values_list('state', flat=True).distinct()

    selected_states = []
    selected_indicator = None
    data = None
    test = None
    state = None
    uri = None  # Corrected initialization

    if request.method == 'GET':
        selected_indicator = request.GET.get('indicator', indicators[0] if indicators else '')
        selected_states = request.GET.getlist('state')

        if selected_indicator and selected_states:
            data = Indicator.objects.filter(indicator=selected_indicator, state__in=selected_states).values()
            df = pd.DataFrame(data)

            print("DataFrame columns:", df.columns)
            if 'state' not in df.columns:
                raise KeyError("'state' column is missing from the DataFrame")
            print("DataFrame dtypes:", df.dtypes)
            print(df.head())
            test = df.head()

            df["Growth"] = df.groupby("state")["value"].pct_change(periods=2) * 100
            pivot_df = df.pivot(index="year", columns="state", values="Growth")

            plt.figure()
            pivot_df.plot(kind="line", marker="o")
            plt.title(f"Year by Year Growth of {selected_indicator} by State")
            plt.xlabel("Year")
            plt.ylabel("Growth (%)")
            plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(4))
            plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x)}'))
            plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2))  # Set major ticks at every 10%
            plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y:.0f}%'))
            plt.legend(title="State")
            plt.grid(True)

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            # string = base64.b64encode(buf.read())
            string = base64.b64encode(buf.read()).decode('utf-8')
            padding_needed = 4 - (len(string) % 4)
            if padding_needed:
                string += '=' * padding_needed
            uri = urllib.parse.quote(string)

    context = {
        'selected_indicator': selected_indicator,
        'indicators': indicators,
        'selected_states': selected_states,
        'states': states,
        'state': state,
        'data': data,
        'test': test,
        'growth_chart': uri
    }

    return render(request, "rankings/test.html", context)
    


def shown_chart(request):
    indicators1 = Indicator.objects.values_list('indicator', flat=True).distinct()
    states1 = Indicator.objects.values_list('state', flat=True).distinct()

    chosen_states = []
    chosen_indicator = None
    data = None
    test = None
    state = None
    uri = None  # Corrected initialization

    if request.method == 'GET':
        chosen_indicator = request.GET.get('indicator', indicators1[0] if indicators1 else '')
        chosen_states = request.GET.getlist('state')

        if chosen_indicator and chosen_states:
            data = Indicator.objects.filter(indicator=chosen_indicator, state__in=chosen_states).values()
            df = pd.DataFrame(data)

            print("DataFrame columns:", df.columns)
            if 'state' not in df.columns:
                raise KeyError("'state' column is missing from the DataFrame")
            print("DataFrame dtypes:", df.dtypes)
            print(df.head())
        

            df["Growth"] = df.groupby("state")["value"].pct_change() * 100
            pivot_df = df.pivot(index="year", columns="state", values="Growth")

            plt.figure(20, 4)
            pivot_df.plot(kind="line", marker="o")
            plt.title(f"Year by Year Growth of {chosen_indicator} by State")
            plt.xlabel("Year")
            plt.ylabel("Growth (%)")
            plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
            plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x)}'))

            plt.legend(title="State")
            plt.grid(True)

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

    context = {
        'chosen_indicator': chosen_indicator,
        'indicators1': indicators1,
        'chosen_states': chosen_states,
        'states1': states1,
        'state': state,
        'data': data,
        'shown_chart': uri
    }

    return render(request, "rankings/indicator_map.html", context)

def calculate_scores(state_values):
    if not state_values:
        return [0] * len(state_values)  # Return a list of zeros if the input list is empty
    
    min_value = min(state_values)
    max_value = max(state_values)
    
    if min_value == max_value:
        return [1] * len(state_values)  # Return a list of ones if all values are the same
    
    scores = []
    for value in state_values:
        score = ((value - min_value) / (max_value - min_value)) * 6 + 1
        scores.append(score)
    
    return scores
   

def score_and_rankings(request):
    validation_result = validate_input(request)
    if isinstance(validation_result, dict):
        states = validation_result['states']
        years = validation_result['years']
        selected_state = validation_result['selected_state']
        year1 = validation_result['year1']
        year2 = validation_result['year2']
        warning_message = validation_result['warning_message']
    else:
        return validation_result  # This will return the rendered response if there's a warning

    growth_data = {}
    rankings_data = []     

    # Initialize dictionaries for growth and rankings
    all_indicators = Indicator.objects.values_list('indicator', flat=True).distinct()
    all_states = Indicator.objects.values_list('state', flat=True).distinct()
    all_names = GroupName.objects.values_list('name', flat=True).distinct()

    # Create a dictionary to map group to weight
    group_to_weight = {index.group: index.weight for index in IndicatorIndex.objects.all()}

    for indicator in all_indicators:
        state_aggregates_year1 = Indicator.objects.filter(year=year1, indicator=indicator).values('state').annotate(total_value=Sum('value'))
        state_aggregates_year2 = Indicator.objects.filter(year=year2, indicator=indicator).values('state').annotate(total_value=Sum('value'))

        state_map_year1 = {item['state']: item['total_value'] for item in state_aggregates_year1}
        state_map_year2 = {item['state']: item['total_value'] for item in state_aggregates_year2}        

        for state in all_states:
            year1_value = state_map_year1.get(state)
            year2_value = state_map_year2.get(state)

            if year1_value is None or year2_value is None:
                continue

            growth = (year2_value - year1_value) / year1_value * 100 if year1_value != 0 else 0
            growth_data[(state, indicator)] = growth

            indicator_details = Indicator.objects.filter(state=state, indicator=indicator).first()
            unit = indicator_details.unit if indicator_details else None
            source = indicator_details.source if indicator_details else None
            group = indicator_details.group if indicator_details else None

            rankings_data.append({
                'state': state,
                'indicator': indicator,
                'year1_value': year1_value,
                'year2_value': year2_value,
                'growth': growth,
                'unit': unit,
                'source': source,
                'group': group,                    
            })

    # Match the first two characters of group in rankings_data with the index in GroupName
    group_names_map = {group.index[:2]: group.name for group in GroupName.objects.all()}

    for data in rankings_data:
        group_prefix = data['group'][:2]
        data['name'] = group_names_map.get(group_prefix, "Unknown")

    for indicator in all_indicators:
        # Filter rankings_data to get only the entries for the current indicator
        indicator_rankings = [data for data in rankings_data if data['indicator'] == indicator]
    
    # rankings individual indicators
        year1_rank = sorted(indicator_rankings, key=lambda x: x['year1_value'], reverse=True)
        year2_rank = sorted(indicator_rankings, key=lambda x: x['year2_value'], reverse=True)
        growth_rank = sorted(indicator_rankings, key=lambda x: x['growth'], reverse=True)

        for index, item in enumerate(year1_rank):
            item['year1_rank'] = index + 1
        for index, item in enumerate(year2_rank):
            item['year2_rank'] = index + 1
        for index, item in enumerate(growth_rank):
            item['growth_rank'] = index + 1
    
    filtered_rankings = [data for data in rankings_data if data['state'] == selected_state]

    sorted_rankings = sorted(filtered_rankings, key=lambda x: x['group'])

    grouped_rankings = {}

    for data in sorted_rankings:
        group_key = data['group'][:2] if data['group'] else 'Other'
        
        # Try to get the group name from the GroupName model
        group_names = GroupName.objects.filter(index=group_key)
        if group_names.exists():
            group_name = group_names.first().name  # Use the first matching object
        else:
            group_name = 'Other'
        
        # Check if the indicator matches any in the IndicatorIndex model
        indicator_exists = IndicatorIndex.objects.filter(indicator=data['indicator']).exists()
        
        if indicator_exists:
            if group_name not in grouped_rankings:
                grouped_rankings[group_name] = []
            grouped_rankings[group_name].append(data)
    
    rankings_detail = {
        'grouped_rankings': grouped_rankings,
        'rankings_data': sorted_rankings
    }
    # end of rankings individual indicators

    # rankings groups of indicators

    for indicator in all_indicators:
        # Filter rankings_data to get only the entries for the current indicator
        indicator_rankings = [data for data in rankings_data if data['indicator'] == indicator]

        # Extract values for year1, year2, and growth
        year1_values = [data['year1_value'] for data in indicator_rankings]
        year2_values = [data['year2_value'] for data in indicator_rankings]
        growth_values = [data['growth'] for data in indicator_rankings]

        # Calculate scores
        scores1 = calculate_scores(year1_values)
        scores2 = calculate_scores(year2_values)
        scoresgr = calculate_scores(growth_values)

        # Add scores to the data entries
        for i, data in enumerate(indicator_rankings):
            data['scores1'] = scores1[i]
            data['scores2'] = scores2[i]
            data['scoresgr'] = scoresgr[i]
    
    # Calculate scores and rankings for each group
    grouped_data = {}
    weighted_sums_scores1 = {}
    weighted_sums_scores2 = {}
    weighted_sums_scoresgr = {}
    total_weights_scores1 = {}
    total_weights_scores2 = {}
    total_weights_scoresgr = {}

    for data in rankings_data:
        state = data['state']
        group_prefix = data['group'][:2]
        scores1 = data['scores1']
        scores2 = data['scores2']
        scoresgr = data['scoresgr']
        name = data['name']
        
        weight = group_to_weight.get(data['group'], 0)  # Match the group with the weight

        if (state, group_prefix) not in grouped_data:
            grouped_data[(state, group_prefix)] = {'total_scores1': 0, 'total_scores2': 0, 'total_scoresgr': 0, 'count': 0, 'name': name}
            weighted_sums_scores1[(state, group_prefix)] = 0
            weighted_sums_scores2[(state, group_prefix)] = 0
            weighted_sums_scoresgr[(state, group_prefix)] = 0
            total_weights_scores1[(state, group_prefix)] = 0
            total_weights_scores2[(state, group_prefix)] = 0
            total_weights_scoresgr[(state, group_prefix)] = 0

        grouped_data[(state, group_prefix)]['total_scores1'] += scores1
        grouped_data[(state, group_prefix)]['total_scores2'] += scores2
        grouped_data[(state, group_prefix)]['total_scoresgr'] += scoresgr
        grouped_data[(state, group_prefix)]['count'] += 1
        
        weighted_sums_scores1[(state, group_prefix)] += scores1 * weight
        weighted_sums_scores2[(state, group_prefix)] += scores2 * weight
        weighted_sums_scoresgr[(state, group_prefix)] += scoresgr * weight
        
        total_weights_scores1[(state, group_prefix)] += weight
        total_weights_scores2[(state, group_prefix)] += weight
        total_weights_scoresgr[(state, group_prefix)] += weight
    
    average_scores = {
        (state, group): {
            'weighted_avg_scores1': weighted_sums_scores1[(state, group)] / total_weights_scores1[(state, group)] if total_weights_scores1[(state, group)] != 0 else 0,
            'weighted_avg_scores2': weighted_sums_scores2[(state, group)] / total_weights_scores2[(state, group)] if total_weights_scores2[(state, group)] != 0 else 0,
            'weighted_avg_scoresgr': weighted_sums_scoresgr[(state, group)] / total_weights_scoresgr[(state, group)] if total_weights_scoresgr[(state, group)] != 0 else 0,
            'name': grouped_data[(state, group)]['name']
        }
        for (state, group), data in grouped_data.items()
    }

    # Convert average_scores to a list of dictionaries for easier template rendering
    average_scores_list = [
        {
            'state': state,
            'group': group,
            'weighted_avg_scores1': scores['weighted_avg_scores1'],
            'weighted_avg_scores2': scores['weighted_avg_scores2'],
            'weighted_avg_scoresgr': scores['weighted_avg_scoresgr'],
            'name': scores['name']
        }
        for (state, group), scores in average_scores.items()
    ]

    # Calculate rankings for each name among all states
    all_names = set(item['name'] for item in average_scores_list)
    for name in all_names:
        name_scores_list = [item for item in average_scores_list if item['name'] == name]

        name_scores_list.sort(key=lambda x: x['weighted_avg_scores1'], reverse=True)        
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_weighted_avg_scores1'] = rank

        name_scores_list.sort(key=lambda x: x['weighted_avg_scores2'], reverse=True)
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_weighted_avg_scores2'] = rank

        name_scores_list.sort(key=lambda x: x['weighted_avg_scoresgr'], reverse=True)
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_weighted_avg_scoresgr'] = rank

    # Filter the results to show only the selected state
    selected_state_scores = [item for item in average_scores_list if item['state'] == selected_state]

    selected_state_scores  = sorted(selected_state_scores , key=lambda x: x['group'])
    # Ending calculate scores and rankings for each group



    return render(request, 'rankings/scores.html', {
        'average_scores_list': selected_state_scores,
        'grouped_rankings': grouped_rankings,
        'rankings_data': sorted_rankings,
        'states': states,
        'years': years,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
    })

