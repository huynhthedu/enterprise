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
import urllib.parse
import matplotlib.ticker as ticker
from django.shortcuts import get_object_or_404


def validate_input(request, template_name):
    # Fetch available states, indicators, and valid years
    states = list(Indicator.objects.values_list('state', flat=True).distinct().order_by('state'))
    years = list(range(1999, 2024))  # Valid years range

    # Initialize variables
    selected_state = None
    year1 = None
    year2 = None
    warning_message = None

    if request.method == 'GET':
        # Fetch inputs with default values
        selected_state = request.GET.get('state', None)
        year1 = request.GET.get('year1', None)
        year2 = request.GET.get('year2', None)

        # Validate state
        # if selected_state not in states:
        #     warning_message = "Invalid state selected. Please choose a valid state."
        # else:
            # Convert years to integers and validate
        try:
            year1 = int(year1) if year1 else min(years)
            year2 = int(year2) if year2 else max(years)

            if year1 not in years or year2 not in years:
                warning_message = "Selected years are out of range. Please choose valid years."
            elif year2 <= year1:
                warning_message = "Year 2 must be greater than Year 1. Please choose another year."
        except ValueError:
            warning_message = "Invalid year format. Please enter valid numbers for years."

    # If there's a warning, return the input form with the warning message
    if warning_message:
        return render(request, template_name, {  # Use the template_name parameter
            'states': states,
            'years': years,
            'selected_state': selected_state,
            'year1': year1,
            'year2': year2,
            'warning_message': warning_message,
            'grouped_rankings': None,
            'rankings_data': None,
        })

    # Return validated data
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

def calculate_ratio(indicator1_id, indicator2_id):
    indicator1 = get_object_or_404(Indicator, group=indicator1_id)
    indicator2 = get_object_or_404(Indicator, group=indicator2_id)

    if indicator2.value == 0:
        return None  # Avoid division by zero

    ratio = indicator1.value / indicator2.value
    return ratio   

def calculate_ratios(pairs, ratio_groups):
    results = []
    for pair, group in zip(pairs, ratio_groups):
        ratio = calculate_ratio(pair[0], pair[1])
        results.append((group, pair[0], pair[1], ratio))
    return results


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
    calculated_indicators = []  # Store generated indicators

    # Initialize dictionaries for growth and rankings
    all_indicators = Indicator.objects.values_list('indicator', flat=True).distinct()
    all_states = Indicator.objects.values_list('state', flat=True).distinct()
    all_names = GroupName.objects.values_list('name', flat=True).distinct()

    # Define pairs and ratio groups
    pairs_of_indicators = [
        ('E47', 'E16'),
        ('E42', 'E16'),
        ('E47', 'E14'),
        ('E51', 'E14'),
        ('E65', 'E11'),
    ]
    ratio_groups = ['E61', 'E62', 'E63', 'E64', 'E66']
    pair_to_group_mapping = {pair: ratio_groups[i] for i, pair in enumerate(pairs_of_indicators)}

    # Step 1: Precompute derived indicators (ratios) with assigned groups
    for state in all_states:
        for id1, id2 in pairs_of_indicators:
            value1 = Indicator.objects.filter(state=state, group=id1, year=year1).aggregate(Sum('value'))['value__sum']
            value2 = Indicator.objects.filter(state=state, group=id2, year=year1).aggregate(Sum('value'))['value__sum']

            if value1 is not None and value2 not in (None, 0):
                calculated_indicators.append({
                    'state': state,
                    'indicator': f"{id1}_to_{id2}_ratio",  # Naming convention for the new indicator
                    'value': value1 / value2,
                    'year': year1,
                    'group': pair_to_group_mapping.get((id1, id2))  # Assign the corresponding group
                })

    # Add calculated indicators to the list of indicators for processing
    all_indicators = list(all_indicators) + [ci['indicator'] for ci in calculated_indicators]


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
    weighted_scores1 = {}
    weighted_scores2 = {}
    weighted_scoresgr = {}
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
            weighted_scores1[(state, group_prefix)] = 0
            weighted_scores2[(state, group_prefix)] = 0
            weighted_scoresgr[(state, group_prefix)] = 0
            total_weights_scores1[(state, group_prefix)] = 0
            total_weights_scores2[(state, group_prefix)] = 0
            total_weights_scoresgr[(state, group_prefix)] = 0

        grouped_data[(state, group_prefix)]['total_scores1'] += scores1
        grouped_data[(state, group_prefix)]['total_scores2'] += scores2
        grouped_data[(state, group_prefix)]['total_scoresgr'] += scoresgr
        grouped_data[(state, group_prefix)]['count'] += 1
        
        weighted_scores1[(state, group_prefix)] += scores1 * weight
        weighted_scores2[(state, group_prefix)] += scores2 * weight
        weighted_scoresgr[(state, group_prefix)] += scoresgr * weight
        
        total_weights_scores1[(state, group_prefix)] += weight
        total_weights_scores2[(state, group_prefix)] += weight
        total_weights_scoresgr[(state, group_prefix)] += weight
    
    average_scores = {
        (state, group): {
            'avg_scores1': weighted_scores1[(state, group)] / total_weights_scores1[(state, group)] if total_weights_scores1[(state, group)] != 0 else 0,
            'avg_scores2': weighted_scores2[(state, group)] / total_weights_scores2[(state, group)] if total_weights_scores2[(state, group)] != 0 else 0,
            'avg_scoresgr': weighted_scoresgr[(state, group)] / total_weights_scoresgr[(state, group)] if total_weights_scoresgr[(state, group)] != 0 else 0,
            'name': grouped_data[(state, group)]['name']
        }
        for (state, group), data in grouped_data.items()
    }

    # Convert average_scores to a list of dictionaries for easier template rendering
    average_scores_list = [
        {
            'state': state,
            'group': group,
            'avg_scores1': scores['avg_scores1'],
            'avg_scores2': scores['avg_scores2'],
            'avg_scoresgr': scores['avg_scoresgr'],
            'name': scores['name']
        }
        for (state, group), scores in average_scores.items()
    ]

    # Calculate rankings for each name among all states
    all_names = set(item['name'] for item in average_scores_list)
    for name in all_names:
        name_scores_list = [item for item in average_scores_list if item['name'] == name]

        name_scores_list.sort(key=lambda x: x['avg_scores1'], reverse=True)        
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_avg_scores1'] = rank

        name_scores_list.sort(key=lambda x: x['avg_scores2'], reverse=True)
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_avg_scores2'] = rank

        name_scores_list.sort(key=lambda x: x['avg_scoresgr'], reverse=True)
        for rank, item in enumerate(name_scores_list, start=1):
            item['rank_avg_scoresgr'] = rank

    # Filter the results to show only the selected state
    selected_state_scores = [item for item in average_scores_list if item['state'] == selected_state]

    selected_state_scores  = sorted(selected_state_scores , key=lambda x: x['group'])
    # Ending calculate scores and rankings for each group


# Calculate scores and rankings for each state
    state_data = {}
    weighted_sums_scores1 = {}
    weighted_sums_scores2 = {}
    weighted_sums_scoresgr = {}
    state_weights_scores1 = {}
    state_weights_scores2 = {}
    state_weights_scoresgr = {}

    for data in rankings_data:
        state = data['state']
        scores1 = data['scores1']
        scores2 = data['scores2']
        scoresgr = data['scoresgr']        
        
        weight = group_to_weight.get(data['group'], 0)  # Match the group with the weight

        if (state) not in state_data:
            state_data[(state)] = {'state_scores1': 0, 'state_scores2': 0, 'state_scoresgr': 0, 'count': 0}
            weighted_sums_scores1[(state)] = 0
            weighted_sums_scores2[(state)] = 0
            weighted_sums_scoresgr[(state)] = 0
            state_weights_scores1[(state)] = 0
            state_weights_scores2[(state)] = 0
            state_weights_scoresgr[(state)] = 0

        state_data[(state)]['state_scores1'] += scores1
        state_data[(state)]['state_scores2'] += scores2
        state_data[(state)]['state_scoresgr'] += scoresgr
        state_data[(state)]['count'] += 1
        
        weighted_sums_scores1[(state)] += scores1 * weight
        weighted_sums_scores2[(state)] += scores2 * weight
        weighted_sums_scoresgr[(state)] += scoresgr * weight
        
        state_weights_scores1[(state)] += weight
        state_weights_scores2[(state)] += weight
        state_weights_scoresgr[(state)] += weight
    
    average_scores = {
        (state): {
            'weighted_avg_scores1': weighted_sums_scores1[(state)] / state_weights_scores1[(state)] if state_weights_scores1[(state)] != 0 else 0,
            'weighted_avg_scores2': weighted_sums_scores2[(state)] / state_weights_scores2[(state)] if state_weights_scores2[(state)] != 0 else 0,
            'weighted_avg_scoresgr': weighted_sums_scoresgr[(state)] / state_weights_scoresgr[(state)] if state_weights_scoresgr[(state)] != 0 else 0,            
        }
        for (state), data in state_data.items()
    }

    # Convert average_scores to a list of dictionaries for easier template rendering
    state_average_scores_list = [
        {
            'state': state,
            'weighted_avg_scores1': scores['weighted_avg_scores1'],
            'weighted_avg_scores2': scores['weighted_avg_scores2'],
            'weighted_avg_scoresgr': scores['weighted_avg_scoresgr'],            
        }
        for (state), scores in average_scores.items()
    ]

    # Calculate rankings for each name among all states
    state_scores_list = [item for item in state_average_scores_list ]

    state_scores_list.sort(key=lambda x: x['weighted_avg_scores1'], reverse=True)        
    for rank, item in enumerate(state_scores_list, start=1):
        item['rank_weighted_avg_scores1'] = rank

    state_scores_list.sort(key=lambda x: x['weighted_avg_scores2'], reverse=True)
    for rank, item in enumerate(state_scores_list, start=1):
        item['rank_weighted_avg_scores2'] = rank

    state_scores_list.sort(key=lambda x: x['weighted_avg_scoresgr'], reverse=True)
    for rank, item in enumerate(state_scores_list, start=1):
        item['rank_weighted_avg_scoresgr'] = rank

    # Filter the results to show only the selected state
    overall_state_scores = [item for item in state_average_scores_list if item['state'] == selected_state]
    
    # Ending calculate scores and rankings for each state

    return render(request, 'rankings/scores.html', {
        'overall_state_scores': overall_state_scores,
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


def result(request):
    
    # 1. Choose one state and two years with function validate_input(request)
    validation_result = validate_input(request, 'rankings.html' )
    if isinstance(validation_result, dict):
        states = validation_result['states']
        years = validation_result['years']
        selected_state = validation_result['selected_state']
        year1 = validation_result['year1']
        year2 = validation_result['year2']
        warning_message = validation_result['warning_message']
    else:
        return validation_result  # Rendered response if there's a warning
    
    # 2. create a dataframe 
    fields = ['group', 'state', 'year', 'value']
    queryset = Indicator.objects.filter(year=year1).values(*fields) | Indicator.objects.filter(year=year2).values(*fields)
    
    # Convert QuerySet to a list of dictionaries
    data = list(queryset)

    # Create a DataFrame
    df = pd.DataFrame(data)    
    df = df.dropna()
    
 
    # 3. Canculate new indicatiors by ratios of existing indicators and add to the dataframe
    new_groups = {
        ('E47', 'E16'): ('E61'),
        ('E42', 'E16'): ('E62'),
        ('E47', 'E14'): ('E63'),
        ('E51', 'E14'): ('E64'),
        ('E65', 'E11'): ('E66'),
    }

    new_rows = []
    for (group1, group2), (new_group_id) in new_groups.items():
        df_group1 = df[df['group'] == group1]
        df_group2 = df[df['group'] == group2]         
        
        if df_group1.empty or df_group2.empty:
            continue  # Skip if either group is empty
       
        merged_df = pd.merge(df_group1, df_group2, on=['state',  'year'], suffixes=('_1', '_2'))          
        
        if merged_df.empty:
            continue  # Skip if merge results in an empty DataFrame
        
        merged_df['value'] = merged_df.apply(
            lambda row: row['value_1'] / row['value_2']*100 if row['value_2'] != 0 else float('nan'), axis=1)
        
        for _, row in merged_df.iterrows():
            new_row = {
                'group': new_group_id,
                'state': row['state'],                
                'year': row['year'],
                'value': row['value']
            }
            new_rows.append(new_row)

    new_rows_df = pd.DataFrame(new_rows)
    df = pd.concat([df, new_rows_df], ignore_index=True)
    df.loc[df['group'] == 'E66', 'value'] *= 100

    # 4. Calculate growth between the two selected years for each indicator
    df = df.pivot_table(index=['state', 'group' ], columns='year', values='value').reset_index()
  
    def calculate_growth(row):
            try:
                if row[year1] != 0:
                    return ((row[year2] - row[year1]) / row[year1]) * 100
                else:
                    return float('nan')
            except KeyError as e:
                print(f"KeyError: {e}")
                return float('nan')

    df['growth'] = df.apply(calculate_growth, axis=1)    
    new_column_names = ['state', 'group', 'value1', 'value2', 'growth']
    df.columns = new_column_names
        
    # 5. caculate score for each indicator among states. The lowest value gets 1.0 and the highest get 7.0, the rankings
    indicators = IndicatorIndex.objects.all().values('group', 'indicator', 'weight', 'unit', 'key')
    indicators_df = pd.DataFrame(list(indicators))
    group_name = GroupName.objects.all().values('index', 'name')
    group_name_df = pd.DataFrame(list(group_name))
    df = pd.merge(df, indicators_df, on=['group'])


    def calculate_scores(state_values, key_values):
        min_value = state_values.min()
        max_value = state_values.max()
        
        if min_value == max_value:
            return pd.Series([1] * len(state_values), index=state_values.index)  # Return a series of ones if all values are the same
        
        scores = pd.Series(index=state_values.index, dtype=float)
        
        for i in range(len(state_values)):
            if key_values.iloc[i] == 1:
                scores.iloc[i] = ((state_values.iloc[i] - min_value) / (max_value - min_value)) * 6 + 1
            elif key_values.iloc[i] == 0:
                scores.iloc[i] = 7 - ((state_values.iloc[i] - min_value) / (max_value - min_value)) * 6
        
        return scores

    # Eliminate empty or none values
    df = df.dropna()

    # Drop specific rows
    groups_to_drop = ['E65', 'E22', 'E24', 'E15']
    df = df[~df['group'].isin(groups_to_drop)]    

    # Apply the calculate_scores function with the key field
    try:
        df['score1'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value1'], x['key'])).reset_index(level=0, drop=True)
        df['score_gr'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['growth'], x['key'])).reset_index(level=0, drop=True)
        df['score2'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value2'], x['key'])).reset_index(level=0, drop=True)
    except Exception as e:
        print("Error during groupby and apply operations:", e)
    

    df['rank1'] = df.groupby(['group'])['score1'].rank(ascending=False)
    df['rankgr'] =df.groupby(['group'])['score_gr'].rank(ascending=False)
    df['rank2'] = df.groupby(['group'])['score2'].rank(ascending=False)
    
        
    #6. Calculate weighted scores by groups of indicators, and overall then rankings 

    df['index'] = df['group'].str[:2]
    df['index_main'] = df['group'].str[:1]
    indicators_df['group_index'] = indicators_df['group'].str[:2]
    # df = pd.merge(df, indicators_df, on=['group'])
    df['weighted_score1'] = df['score1'] * df['weight']
    df['weighted_score_gr'] = df['score_gr'] * df['weight']
    df['weighted_score2'] = df['score2'] * df['weight']

    # Function to calculate weighted averages with division by zero check
   
    def calculate_weighted_avg(x):
        weight_sum = x['weight'].sum()
        if weight_sum == 0:
            return pd.Series({
                'weighted_avg_score1': float('nan'),                
                'weighted_avg_score_gr': float('nan'),
                'weighted_avg_score2': float('nan')
            })
        else:
            return pd.Series({
                'weighted_avg_score1': x['weighted_score1'].sum() / weight_sum,
                'weighted_avg_score_gr': x['weighted_score_gr'].sum() / weight_sum,
                'weighted_avg_score2': x['weighted_score2'].sum() / weight_sum
            })

    # Calculate the overall weighted average score and growth score for each group and year
    try:
        weighted_avg_scores = df.groupby(['index', 'state']).apply(calculate_weighted_avg).reset_index()
        weighted_avg_scores_state = df.groupby(['index_main', 'state']).apply(calculate_weighted_avg).reset_index()        

        # Merge with group_name_df to get the names
        weighted_avg_scores = pd.merge(weighted_avg_scores, group_name_df, on='index')        
        weighted_avg_scores['weighted_rank1'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores['weighted_rank_gr'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores['weighted_rank2'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score2'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank1'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank_gr'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank2'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score2'].rank(ascending=False)


        weighted_avg_scores = weighted_avg_scores[weighted_avg_scores['state'] == selected_state]
        weighted_avg_scores_state = weighted_avg_scores_state[weighted_avg_scores_state['state'] == selected_state]
        df = df[df['state'] == selected_state]

    except Exception as e:
        print(f"An error occurred: {e}")


    df1_dict = df.to_dict(orient='records')
    df2_dict = weighted_avg_scores.to_dict(orient='records')
    df3_dict = weighted_avg_scores_state.to_dict(orient='records')       

    context = {
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'states': states,
        'years': years,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message
    }
    return render(request, 'rankings/rankings.html', context )



def inputs(request, template_name):
    # Fetch available states, indicators, and valid years
    states = list(Indicator.objects.values_list('state', flat=True).distinct().order_by('state'))
    years = list(range(1999, 2024))  # Valid years range
    indicators = list(IndicatorIndex.objects.filter(weight__gt=0).values_list('indicator', flat=True).distinct().order_by('indicator'))
    print(indicators)

    # Initialize variables
    selected_state = None
    selected_indicators = []
    year1 = None
    year2 = None
    warning_message = None

    if request.method == 'GET':
        # Fetch inputs with default values
        selected_state = request.GET.get('state', None)
        selected_indicators = request.GET.getlist('indicators', [])
        year1 = request.GET.get('year1', None)
        year2 = request.GET.get('year2', None)

        # Validate state
        # if selected_state not in states:
        #     warning_message = "Invalid state selected. Please choose a valid state."
        # else:
            # Convert years to integers and validate
        try:
            year1 = int(year1) if year1 else min(years)
            year2 = int(year2) if year2 else max(years)

            if year1 not in years or year2 not in years:
                warning_message = "Selected years are out of range. Please choose valid years."
            elif year2 <= year1:
                warning_message = "Year 2 must be greater than Year 1. Please choose another year."
        except ValueError:
            warning_message = "Invalid year format. Please enter valid numbers for years."

    # If there's a warning, return the input form with the warning message
    if warning_message:
        return render(request, template_name, {
            'states': states,
            'indicators': indicators,
            'years': years,
            'selected_state': selected_state,
            'selected_indicators': selected_indicators,
            'year1': year1,
            'year2': year2,
            'warning_message': warning_message,
            'grouped_rankings': None,
            'rankings_data': None,
        })

    # Return validated data
    return {
        'states': states,
        'indicators': indicators,
        'years': years,
        'selected_state': selected_state,
        'selected_indicators': selected_indicators,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
    }


def calculations(year1, year2):
    
    # 2. create a dataframe 
    fields = ['group', 'state', 'year', 'value']
    queryset = Indicator.objects.filter(year=year1).values(*fields) | Indicator.objects.filter(year=year2).values(*fields)
    
    # Convert QuerySet to a list of dictionaries
    data = list(queryset)

    # Create a DataFrame
    df = pd.DataFrame(data)    
    df = df.dropna()
    
 
    # 3. Canculate new indicatiors by ratios of existing indicators and add to the dataframe
    new_groups = {
        ('E47', 'E16'): ('E61'),
        ('E42', 'E16'): ('E62'),
        ('E47', 'E14'): ('E63'),
        ('E51', 'E14'): ('E64'),
        ('E65', 'E11'): ('E66'),
    }

    new_rows = []
    for (group1, group2), (new_group_id) in new_groups.items():
        df_group1 = df[df['group'] == group1]
        df_group2 = df[df['group'] == group2]         
        
        if df_group1.empty or df_group2.empty:
            continue  # Skip if either group is empty
       
        merged_df = pd.merge(df_group1, df_group2, on=['state',  'year'], suffixes=('_1', '_2'))          
        
        if merged_df.empty:
            continue  # Skip if merge results in an empty DataFrame
        
        merged_df['value'] = merged_df.apply(
            lambda row: row['value_1'] / row['value_2']*100 if row['value_2'] != 0 else float('nan'), axis=1)
        
        for _, row in merged_df.iterrows():
            new_row = {
                'group': new_group_id,
                'state': row['state'],                
                'year': row['year'],
                'value': row['value']
            }
            new_rows.append(new_row)

    new_rows_df = pd.DataFrame(new_rows)
    df = pd.concat([df, new_rows_df], ignore_index=True)
    df.loc[df['group'] == 'E66', 'value'] *= 100

    # 4. Calculate growth between the two selected years for each indicator
    df = df.pivot_table(index=['state', 'group' ], columns='year', values='value').reset_index()
  
    def calculate_growth(row):
            try:
                if row[year1] != 0:
                    return ((row[year2] - row[year1]) / row[year1]) * 100
                else:
                    return float('nan')
            except KeyError as e:
                print(f"KeyError: {e}")
                return float('nan')

    df['growth'] = df.apply(calculate_growth, axis=1)    
    new_column_names = ['state', 'group', 'value1', 'value2', 'growth']
    df.columns = new_column_names
        
    # 5. caculate score for each indicator among states. The lowest value gets 1.0 and the highest get 7.0, the rankings
    indicators = IndicatorIndex.objects.all().values('group', 'indicator', 'weight', 'unit', 'key')
    indicators_df = pd.DataFrame(list(indicators))
    group_name = GroupName.objects.all().values('index', 'name')
    group_name_df = pd.DataFrame(list(group_name))
    df = pd.merge(df, indicators_df, on=['group'])


    def calculate_scores(state_values, key_values):
        min_value = state_values.min()
        max_value = state_values.max()
        
        if min_value == max_value:
            return pd.Series([1] * len(state_values), index=state_values.index)  # Return a series of ones if all values are the same
        
        scores = pd.Series(index=state_values.index, dtype=float)
        
        for i in range(len(state_values)):
            if key_values.iloc[i] == 1:
                scores.iloc[i] = ((state_values.iloc[i] - min_value) / (max_value - min_value)) * 6 + 1
            elif key_values.iloc[i] == 0:
                scores.iloc[i] = 7 - ((state_values.iloc[i] - min_value) / (max_value - min_value)) * 6
        
        return scores

    # Eliminate empty or none values
    df = df.dropna()

    # Drop specific rows
    groups_to_drop = ['E65', 'E22', 'E24', 'E15']
    df = df[~df['group'].isin(groups_to_drop)]    

    # Apply the calculate_scores function with the key field
    try:
        df['score1'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value1'], x['key'])).reset_index(level=0, drop=True)
        df['score_gr'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['growth'], x['key'])).reset_index(level=0, drop=True)
        df['score2'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value2'], x['key'])).reset_index(level=0, drop=True)
    except Exception as e:
        print("Error during groupby and apply operations:", e)
    

    df['rank1'] = df.groupby(['group'])['score1'].rank(ascending=False)
    df['rankgr'] =df.groupby(['group'])['score_gr'].rank(ascending=False)
    df['rank2'] = df.groupby(['group'])['score2'].rank(ascending=False)
    
        
    #6. Calculate weighted scores by groups of indicators, and overall then rankings 

    df['index'] = df['group'].str[:2]
    df['index_main'] = df['group'].str[:1]
    indicators_df['group_index'] = indicators_df['group'].str[:2]
    # df = pd.merge(df, indicators_df, on=['group'])
    df['weighted_score1'] = df['score1'] * df['weight']
    df['weighted_score_gr'] = df['score_gr'] * df['weight']
    df['weighted_score2'] = df['score2'] * df['weight']

    # Function to calculate weighted averages with division by zero check
   
    def calculate_weighted_avg(x):
        weight_sum = x['weight'].sum()
        if weight_sum == 0:
            return pd.Series({
                'weighted_avg_score1': float('nan'),                
                'weighted_avg_score_gr': float('nan'),
                'weighted_avg_score2': float('nan')
            })
        else:
            return pd.Series({
                'weighted_avg_score1': x['weighted_score1'].sum() / weight_sum,
                'weighted_avg_score_gr': x['weighted_score_gr'].sum() / weight_sum,
                'weighted_avg_score2': x['weighted_score2'].sum() / weight_sum
            })

    # Calculate the overall weighted average score and growth score for each group and year
    try:
        weighted_avg_scores = df.groupby(['index', 'state']).apply(calculate_weighted_avg).reset_index()
        weighted_avg_scores_state = df.groupby(['index_main', 'state']).apply(calculate_weighted_avg).reset_index()        

        # Merge with group_name_df to get the names
        weighted_avg_scores = pd.merge(weighted_avg_scores, group_name_df, on='index')        
        weighted_avg_scores['weighted_rank1'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores['weighted_rank_gr'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores['weighted_rank2'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score2'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank1'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank_gr'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores_state['weighted_state_rank2'] = weighted_avg_scores_state.groupby(['index_main'])['weighted_avg_score2'].rank(ascending=False)

    except Exception as e:
        print(f"An error occurred: {e}")



    context = {
        'df': df,
        'weighted_avg_scores': weighted_avg_scores,
        'weighted_avg_scores_state': weighted_avg_scores_state,
    }
    return context

def doanhnghiep(request):
    input_data = inputs(request, 'doanhnghiep.html')
    if isinstance(input_data, dict):
        states = input_data['states']
        years = input_data['years']
        indicators = input_data['indicators']
        selected_indicators = input_data['selected_indicators']
        selected_state = input_data['selected_state']
        year1 = input_data['year1']
        year2 = input_data['year2']
        warning_message = input_data['warning_message']
    else:
        return input_data  # Rendered response if there's a warning

    # Perform calculations
    calculations_result = calculations(year1, year2)
    df = calculations_result['df']
    weighted_avg_scores = calculations_result['weighted_avg_scores']
    weighted_avg_scores_state = calculations_result['weighted_avg_scores_state']

    # Order the DataFrame by group
    df = df.sort_values(by='group')

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        plt.figure(figsize=(10, 15))
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value2', ascending=True)
        
        # Create a new column combining state names and rank2 with no decimal
        indicator_df['state_rank'] = indicator_df.apply(lambda row: f"{row['state']} (Rank: {int(row['rank2'])})", axis=1)
        
        bars = plt.barh(indicator_df['state_rank'], indicator_df['value2'], label=indicator)
        
        # Highlight the border of the selected state and show data in bars with one decimal
        for bar, state, value2, rank2 in zip(bars, indicator_df['state'], indicator_df['value2'], indicator_df['rank2']):
            if rank2 <= 10:
                bar.set_color('green')
            elif rank2 <= 20:
                bar.set_color('lightgreen')
            elif rank2 <= 30:
                bar.set_color('yellow')
            elif rank2 <= 40:
                bar.set_color('orange')
            else:
                bar.set_color('red')
            
            if state == selected_state:
                bar.set_edgecolor('black')
                bar.set_linewidth(2)
            
            plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{value2:.1f}', va='center', ha='left')

        plt.xlabel('Score')
        plt.ylabel('State')
        plt.title(f'{indicator}')
        
        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the plot as a base64 string
        plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
        plot_urls.append(plot_url)
    
        plt.close()

    # Prepare context for rendering
    weighted_avg_scores_selected_state = weighted_avg_scores[weighted_avg_scores['state'] == selected_state]
    weighted_avg_scores_state_selected_state = weighted_avg_scores_state[weighted_avg_scores_state['state'] == selected_state]
    df_selected_state = df[df['state'] == selected_state]

    df1_dict = df_selected_state.to_dict(orient='records')
    df2_dict = weighted_avg_scores_selected_state.to_dict(orient='records')
    df3_dict = weighted_avg_scores_state_selected_state.to_dict(orient='records')
    
    context = {
        'df': df,
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'states': states,
        'years': years,
        'indicators': indicators,
        'selected_indicators': selected_indicators,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
        'plot_urls': plot_urls,
    }

    return render(request, 'rankings/doanhnghiep.html', context)

def all_states(request):    
    # Fetch inputs
    input_data = inputs(request, 'all_states.html')
    if isinstance(input_data, dict):
        states = input_data['states']
        years = input_data['years']
        indicators = input_data['indicators']
        selected_state = input_data['selected_state']
        selected_indicators = input_data['selected_indicators']
        year1 = input_data['year1']
        year2 = input_data['year2']
        warning_message = input_data['warning_message']
    else:
        return input_data  # Rendered response if there's a warning
    
    # Perform calculations
    calculations_result = calculations(year1, year2)
    df = calculations_result['df']
    print(df.columns.tolist())

    # Filter the DataFrame for the selected indicators
    filtered_df = df[df['indicator'].isin(selected_indicators)]

    # Order the DataFrame by group
    filtered_df = filtered_df.sort_values(by='group')

    # Draw separate horizontal bar charts for score2 of the selected indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        plt.figure(figsize=(10, 15))
        indicator_df = filtered_df[filtered_df['indicator'] == indicator].sort_values(by='score2', ascending=False)
        
        # Create a new column combining state names and rank2 with no decimal
        indicator_df['state_rank'] = indicator_df.apply(lambda row: f"{row['state']} (Rank: {int(row['rank2'])})", axis=1)
        
        bars = plt.barh(indicator_df['state_rank'], indicator_df['score2'], label=indicator)
        
        # Highlight the border of the selected state and show data in bars with one decimal
        for bar, state, score2, rank2 in zip(bars, indicator_df['state'], indicator_df['score2'], indicator_df['rank2']):
            if rank2 <= 10:
                bar.set_color('green')
            elif rank2 <= 20:
                bar.set_color('lightgreen')
            elif rank2 <= 30:
                bar.set_color('yellow')
            elif rank2 <= 40:
                bar.set_color('orange')
            else:
                bar.set_color('red')
            
            if state == selected_state:
                bar.set_edgecolor('black')
                bar.set_linewidth(2)
            
            plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{score2:.1f}', va='center', ha='left')

        plt.xlabel('Score')
        plt.ylabel('State')
        plt.title(f'{indicator}')
        
        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the plot as a base64 string
        plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
        plot_urls.append(plot_url)
        # print(plot_url)
        print(df)
    
    # Prepare context for rendering
    context = {
        'df': df,
        'states': states,
        'years': years,
        'indicators': indicators,
        'selected_state': selected_state,
        'selected_indicators': selected_indicators,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
        'plot_urls': plot_urls
    }

    return render(request, 'rankings/all_states.html', context)