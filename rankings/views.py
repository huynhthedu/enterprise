from django.db.models import Sum  
from mpl_toolkits.axes_grid1 import make_axes_locatable
from django.http import HttpResponse
import io, os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.use('Agg')
import squarify
import geopandas as gpd
import numpy as np
import fiona
import pandas as pd
import base64, urllib
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Indicator, IndicatorIndex, GroupName, State
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import urllib.parse
import matplotlib.ticker as ticker
from django.shortcuts import get_object_or_404
from .forms import StateSelectionForm
from django.http import JsonResponse, HttpResponseBadRequest


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


def inputs(request, template_name):
    # Fetch available states, indicators, and valid years
    states = list(Indicator.objects.values_list('state', flat=True).distinct().order_by('state'))
    years = list(range(1999, 2024))  # Valid years range
    indicators = list(IndicatorIndex.objects.filter(weight__gt=0).values_list('indicator', flat=True).distinct().order_by('group'))
    # print(indicators)

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
    fields = ['group', 'state', 'year', 'value', 'unit']
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

def state(request):    
    # Fetch inputs
    input_data = inputs(request, 'rankings/rankings.html')
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

    def format_value(row):
        if row['unit'] == 'Percent':
            return f"{row['value2']:.2f}"
        else:
            return f"{row['value2']:,.0f}"
        
    def format_value2(value2, unit):
        try:
            value2 = float(value2)
        except (ValueError, TypeError):
            return value2  # Return the original value if conversion fails

        if unit == 'Percent':
            return f"{value2:.2f}"
        else:
            return f"{value2:,.0f}"  
    # Perform calculations
    calculations_result = calculations(year1, year2)
    df = calculations_result['df']
    weighted_avg_scores = calculations_result['weighted_avg_scores']
    weighted_avg_scores_state = calculations_result['weighted_avg_scores_state']
    map_color = calculations_result['weighted_avg_scores_state']

    # Order the DataFrame by group
    df = df.sort_values(by='group')
    # print(df.head)

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value2', ascending=True)
        
            # Skip plotting if indicator_df is empty
        if indicator_df.empty:
            print(f"No data available for indicator: {indicator}")
            continue
        # Create a new column combining state names and rank2 with no decimal
        indicator_df['state_rank'] = indicator_df.apply(lambda row: f"{row['state']} {int(row['rank2'])}", axis=1)
        
        bars = ax.barh(indicator_df['state_rank'], indicator_df['value2'], label=indicator)
        
        # Highlight the border of the selected state and show data in bars with one decimal
        for bar, state, value2, rank2, unit in zip(bars, indicator_df['state'], indicator_df['value2'], indicator_df['rank2'], indicator_df['unit']):
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

            
            formatted_value2 = format_value2(value2, unit)
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, format_value2(value2, unit), va='center', ha='left', fontsize=20)
            # ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{value2:.1f}', va='center', ha='left', fontsize=20)

        ax.set_title(f'{indicator} ({indicator_df["unit"].iloc[0]})', fontsize=30)
        ax.tick_params(axis='both', which='major', labelsize=20)
        
        # Remove the border (spines)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        
        # Remove the x-axis
        ax.get_xaxis().set_visible(False)
        
        # Adjust margins to create more space for tick labels
        plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.1)
        
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
    # print(df.head)

        
    df_selected_state['value2'] = df_selected_state.apply(format_value, axis=1)
    # print(df.head)

    df1_dict = df_selected_state.to_dict(orient='records')
    df2_dict = weighted_avg_scores_selected_state.to_dict(orient='records')
    df3_dict = weighted_avg_scores_state_selected_state.to_dict(orient='records')
    df4_dict = map_color.to_dict(orient='records')
    
    
    context = {
        'df': df,
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'states': states,
        'years': years,
        'db4': df4_dict,
        'indicators': indicators,
        'selected_indicators': selected_indicators,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
        'plot_urls': plot_urls,
    }

    return render(request, 'rankings/rankings.html', context)


def select_state(request):
    # Fetch inputs
    input_data = inputs(request, 'rankings/select_state.html')
    if isinstance(input_data, dict):
        states = input_data['states']
        years = input_data['years']
        indicators = input_data['indicators']
        selected_indicators = input_data['selected_indicators'] or ['Gross Domestic Product']  # Default indicator
        selected_state = input_data['selected_state'] or 'Indiana'  # Default state
        year1 = input_data['year1'] or 2019  # Default year1
        year2 = input_data['year2'] or 2023  # Default year2
        warning_message = input_data['warning_message']
    else:
        return input_data  # Rendered response if there's a warning

    calculations_result = calculations(year1, year2)
    df = calculations_result['df']
    weighted_avg_scores = calculations_result['weighted_avg_scores']
    weighted_avg_scores_state = calculations_result['weighted_avg_scores_state']
    map_color = calculations_result['weighted_avg_scores_state']

    # Order the DataFrame by group
    df = df.sort_values(by='group')
    state_id = State.objects.all().values('name', 's_id')
    state_df = pd.DataFrame(list(state_id))
    df = pd.merge(df, state_df, left_on='state', right_on='name')
    # print(df.head)

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value2', ascending=True)

        if indicator_df.empty:
            print(f"No data available for indicator: {indicator}")
            continue
        
        # Create a new column combining state names and rank2 with no decimal
        indicator_df['state_rank'] = indicator_df.apply(lambda row: f"{row['state']} {int(row['rank2'])}", axis=1)
        
        bars = ax.barh(indicator_df['state_rank'], indicator_df['value2'], label=indicator)
        
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
            
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{value2:.1f}', va='center', ha='left', fontsize=20)

        ax.set_title(f'{indicator} ({indicator_df["unit"].iloc[0]})', fontsize=30)
        ax.tick_params(axis='both', which='major', labelsize=20)
        
        # Remove the border (spines)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        
        # Remove the x-axis
        ax.get_xaxis().set_visible(False)
        
        # Adjust margins to create more space for tick labels
        plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.1)
        
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
    df4_dict = map_color.to_dict(orient='records')
    
    
    context = {
        'df': df,
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'df4': df4_dict,
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

    return render(request, 'rankings/select_state.html', context)
    



def one_year(request, pk):
    # Fetch available states, indicators, and valid years
    states = list(Indicator.objects.values_list('state', flat=True).distinct().order_by('state')) 
    years = list(Indicator.objects.values_list('year', flat=True).distinct().order_by('year'))
    indicators = list(IndicatorIndex.objects.filter(weight__gt=0).values_list('indicator', flat=True).distinct().order_by('group'))

    # Initialize variables
    selected_state = None
    selected_indicators = []
    year = None    
    warning_message = None

    if request.method == 'GET':
        # Fetch inputs with default values        
        year = request.GET.get('year', 2023)        
        selected_indicators = request.GET.getlist('indicators', [])

    fields = ['group', 'state', 'year', 'value']
    queryset = Indicator.objects.filter(year=year).values(*fields)     
     
    data = list(queryset)    
    # Create a DataFrame
    df = pd.DataFrame(data)    
    df = df.dropna()    

    # Calculate new indicators by ratios of existing indicators and add to the dataframe
    new_groups = {
        ('E47', 'E16'): 'E61',
        ('E42', 'E16'): 'E62',
        ('E47', 'E14'): 'E63',
        ('E51', 'E14'): 'E64',
        ('E65', 'E11'): 'E66',
    }

    new_rows = []
    for (group1, group2), new_group_id in new_groups.items():
        df_group1 = df[df['group'] == group1]
        df_group2 = df[df['group'] == group2]         

        if df_group1.empty or df_group2.empty:
            continue  # Skip if either group is empty

        merged_df = pd.merge(df_group1, df_group2, on=['state', 'year'], suffixes=('_1', '_2'))          

        if merged_df.empty:
            continue  # Skip if merge results in an empty DataFrame

        merged_df['value'] = merged_df.apply(
            lambda row: row['value_1'] / row['value_2'] * 100 if row['value_2'] != 0 else float('nan'), axis=1)

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

    indicators1 = IndicatorIndex.objects.all().values('group', 'indicator', 'weight', 'unit', 'key')
    indicators_df = pd.DataFrame(list(indicators1))    
    df = pd.merge(df, indicators_df, on=['group'])
    state_id = State.objects.all().values('name', 's_id')
    state_df = pd.DataFrame(list(state_id))
    df = pd.merge(df, state_df, left_on='state', right_on='name')
    df['rank'] = df.groupby(['group'])['value'].rank(ascending=False)
    # print(df.head)

    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(32, 16))  # Increase figure size
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value', ascending=False)
     
        if indicator_df.empty:
            print(f"No data available for indicator: {indicator}")
            continue
     
        # Create a new column combining state names and rank with no decimal
        indicator_df['rank'] = indicator_df.groupby(['group'])['value'].rank(ascending=False)
     
        indicator_df['state_rank'] = indicator_df.apply(
        lambda row: f"{row['state']}\n{row['value']:,.0f}" if row['unit'] != "Percent" else f"{row['state']}\n{row['value']:.2f}%", 
        axis=1
        )
            
        # Prepare data for the tree map
        sizes = indicator_df['value'].tolist()        
        labels = indicator_df['state_rank'].tolist()
        colors = ['green' if rank <= 10 else 'lightgreen' if rank <= 20 else 'yellow' if rank <= 30 else 'orange' if rank <= 40 else 'red' for rank in indicator_df['rank']]        
     
        # Ensure no zero sizes to avoid ZeroDivisionError
        sizes = [size if size > 0 else 0.1 for size in sizes]
     
        # Create the tree map
        squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, ax=ax, edgecolor="black", linewidth=1.5)
     
        ax.set_title(f'{indicator} ({indicator_df["unit"].iloc[0]})', fontsize=30, pad=50)
        ax.axis('off')  # Remove axes
     
        # Increase label font size
        for label in ax.texts:
            label.set_fontsize(20)
     
        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
     
        # Encode the plot as a base64 string
        plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
        plot_urls.append(plot_url)

        plt.close()

    context = {
        'df': df,
        'states': states,
        'years': years,
        'indicators': indicators,
        'selected_indicators': selected_indicators,        
        'year': year,        
        'warning_message': warning_message,
        'plot_urls': plot_urls,
    }

    return render(request, 'rankings/one_year.html', context)

    



def data_prepare():
    fields = ['group', 'state', 'year', 'value']
    queryset = Indicator.objects.values(*fields)
    
    data = list(queryset)

    # Create a DataFrame
    df = pd.DataFrame(data)
    df = df.dropna()

    # Check if the required columns exist
    required_columns = ['group', 'state', 'year', 'value']
    if not all(column in df.columns for column in required_columns):
        raise KeyError(f"One or more required columns are missing in the DataFrame: {required_columns}")

    # Calculate new indicators by ratios of existing indicators and add to the DataFrame
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
        
        merged_df = pd.merge(df_group1, df_group2, on=['state', 'year'], suffixes=('_1', '_2'))
        
        if merged_df.empty:
            continue  # Skip if merge results in an empty DataFrame
        
        merged_df['value'] = merged_df.apply(
            lambda row: row['value_1'] / row['value_2'] * 100 if row['value_2'] != 0 else float('nan'), axis=1)
        
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
    df['growth'] = df.groupby(['group', 'state'])['value'].pct_change() * 100
    # Generate rankings for each indicator by state and year
    df['rankings'] = df.groupby(['group', 'year'])['value'].rank(ascending=False, method='dense')
    df.sort_values(by=['group', 'state', 'year'], inplace=True)
    # Reset index
    df.reset_index(drop=True, inplace=True)
    # print(df.columns)
    # print(df.head)
    
    indicators1 = IndicatorIndex.objects.all().values('group', 'indicator', 'weight', 'unit', 'key')
    indicators_df = pd.DataFrame(list(indicators1))    
    df = pd.merge(df, indicators_df, on=['group'])
    state_id = State.objects.all().values('name', 's_id')
    state_df = pd.DataFrame(list(state_id))
    df = pd.merge(df, state_df, left_on='state', right_on='name')    
    # print(df.columns)
    # print(df.head)

    context = {
        'df': df,
    }
    return context



def dashboard_view(request):
    # Fetch inputs
    states = list(Indicator.objects.values_list('state', flat=True).distinct().order_by('state'))
    years = list(range(1999, 2024))  # Valid years range
    indicators = list(IndicatorIndex.objects.filter(weight__gt=0).values_list('indicator', flat=True).distinct().order_by('group'))

    # Initialize variables
    selected_state = 'Indiana'
    selected_indicators = ['Gross Domestic Product', 'Population']
    year1 = 2019
    year2 = 2023
    warning_message = None

    if request.method == 'GET':
        # Fetch inputs with default values
        selected_state = request.GET.get('state', selected_state)
        selected_indicators = request.GET.getlist('indicators', selected_indicators)
        year1 = request.GET.get('year1', year1)
        year2 = request.GET.get('year2', year2)

        # Validate state
        try:
            year1 = int(year1) if year1 else min(years)
            year2 = int(year2) if year2 else max(years)

            if year1 not in years or year2 not in years:
                warning_message = "Selected years are out of range. Please choose valid years."
            elif year2 <= year1:
                warning_message = "Year 2 must be greater than Year 1. Please choose another year."
        except ValueError:
            warning_message = "Invalid year format. Please enter valid numbers for years."

    def format_value(row):
        if row['unit'] == 'Percent':
            return f"{row['value2']:.2f}"
        else:
            return f"{row['value2']:,.0f}"
        
    def format_value2(value2, unit):
        try:
            value2 = float(value2)
        except (ValueError, TypeError):
            return value2  # Return the original value if conversion fails

        if unit == 'Percent':
            return f"{value2:.2f}"
        else:
            return f"{value2:,.0f}"  

    # Perform calculations
    calculations_result = calculations(year1, year2)
    df = calculations_result['df']
    weighted_avg_scores = calculations_result['weighted_avg_scores']
    weighted_avg_scores_state = calculations_result['weighted_avg_scores_state']
    map_color = calculations_result['weighted_avg_scores_state']

    # Order the DataFrame by group
    df = df.sort_values(by='group')

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value2', ascending=True)
        
        # Skip plotting if indicator_df is empty
        if indicator_df.empty:
            print(f"No data available for indicator: {indicator}")
            continue

        # Create a new column combining state names and rank2 with no decimal
        indicator_df['state_rank'] = indicator_df.apply(lambda row: f"{row['state']} {int(row['rank2'])}", axis=1)
        
        bars = ax.barh(indicator_df['state_rank'], indicator_df['value2'], label=indicator)
        
        # Highlight the border of the selected state and show data in bars with one decimal
        for bar, state, value2, rank2, unit in zip(bars, indicator_df['state'], indicator_df['value2'], indicator_df['rank2'], indicator_df['unit']):
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

            formatted_value2 = format_value2(value2, unit)
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, formatted_value2, va='center', ha='left', fontsize=20)

        ax.set_title(f'{indicator} ({indicator_df["unit"].iloc[0]})', fontsize=30)
        ax.tick_params(axis='both', which='major', labelsize=20)
        
        # Remove the border (spines)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        
        # Remove the x-axis
        ax.get_xaxis().set_visible(False)
        
        # Adjust margins to create more space for tick labels
        plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.1)
        
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

    df_selected_state['value2'] = df_selected_state.apply(format_value, axis=1)

    df1_dict = df_selected_state.to_dict(orient='records')
    df2_dict = weighted_avg_scores_selected_state.to_dict(orient='records')
    df3_dict = weighted_avg_scores_state_selected_state.to_dict(orient='records')
    df4_dict = map_color.to_dict(orient='records')


    context = data_prepare()
    data = context['df'][context['df']['state'] == selected_state]
    year = data['year'].max()
    
    # Generate pie charts
    pie_charts_url = generate_pie_charts(data)
    bar_charts_url = generate_bar_charts(data)
    
    context.update({
        'data': data,
        'year': year,
        'df': df,
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'states': states,
        'years': years,
        'db4': df4_dict,
        'indicators': indicators,
        'selected_indicators': selected_indicators,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message,
        'plot_urls': plot_urls,
        'pie_charts_url': pie_charts_url,  # Add the pie charts URL to the context
        'bar_charts_url': bar_charts_url,  # Add the pie charts URL to the context
    })

    return render(request, 'rankings/dashboard.html', context)

def get_indicator_data(request):
    default_indicator = 'Gross Domestic Product'  # Set your default indicator here
    indicator = request.GET.get('indicator', default_indicator).strip()
    state = request.GET.get('state')

    if not state:
        return HttpResponseBadRequest("Missing 'state' parameter")

    context = data_prepare()
    df = context['df']  # Access the DataFrame from the context dictionary      

    # Filter and sort the DataFrame
    data = df[(df['indicator'] == indicator) & (df['state'] == state)].sort_values(by='year')
    
    # Extract years and values
    years = data['year'].tolist()
    values = data['value'].tolist()

    return JsonResponse({'years': years, 'values': values, 'default_indicator': default_indicator})


# def get_year_data(request):
#     indicator = request.GET.get('indicator')
#     year = request.GET.get('year')

#     data = Indicator.objects.filter(indicator=indicator, year=year).order_by('state')
#     states = list(data.values_list('state', flat=True))
#     values = list(data.values_list('value', flat=True))

#     return JsonResponse({'states': states, 'values': values})



def get_year_data(request):
    indicator = request.GET.get('indicator').strip()
    year = request.GET.get('year', 2023).strip()

    if not indicator or not year:
        return HttpResponseBadRequest("Missing 'indicator' or 'year' parameter")

    year = int(year)  # Convert year to integer

    context = data_prepare()
    df = context['df']  # Access the DataFrame from the context dictionary

    # Check if the required columns exist
    required_columns = ['indicator', 'year', 'state', 'value']
    if not all(column in df.columns for column in required_columns):
        return HttpResponseBadRequest("Required columns are missing in the DataFrame")

    # Strip spaces from DataFrame values and ensure correct data types
    df['indicator'] = df['indicator'].str.strip()
    df['year'] = df['year'].astype(int)

    # Filter the DataFrame
    filtered_data = df[(df['indicator'] == indicator) & (df['year'] == year)]
    

    # Sort the DataFrame
    data = filtered_data.sort_values(by='value')

    # Extract states and values
    states = data['state'].tolist()
    values = data['value'].tolist()

    return JsonResponse({'states': states, 'values': values})

def overall_indicator(request):

    context = data_prepare()
    df = context['df']  # Access the DataFrame from the context dictionary
    year = df['year'].max()
    print(year)


    context = {
        'df': df,
    }
    return render(request, 'rankings/dashboard.html', context)

def generate_pie_charts(data):
    # Define the indicators to plot
    indicators = ['Gross Domestic Product', 'Employment', 'State revenue']

    # Create a figure with subplots
    fig = plt.figure(figsize=(10, 8))

    # Add a title for the whole chart
    fig.suptitle('Size of the Economy', fontsize=20)

    # Plot each indicator in a triangle position
    sizes = [0.6, 0.4, 0.35]  # Sizes for the pies: GDP is 30%, Employment is 20%, Personal Income Tax is 15%

    # Adjust positions to make pies touch each other
    positions = [(0.3 - sizes[0]/2, 0.3 - sizes[0]/2), 
                 (0.3 + sizes[0]/2 - sizes[1]/2, 0.5 - sizes[1]/2), 
                 (0.3 - sizes[2]/2, 0.4 + sizes[0]/2 - sizes[2]/2)]

    for i, indicator in enumerate(indicators):
        # Get the latest year with data available for the indicator
        latest_year = data[data['indicator'] == indicator]['year'].max()

        # Filter the DataFrame for the selected indicator and latest year
        filtered_df = data[(data['indicator'] == indicator) & (data['year'] == latest_year)]

        # Determine the unit based on the indicator
        unit = "M" if indicator in ['Gross Domestic Product', 'State revenue'] else "person"

        # Create labels with value, unit, rankings, growth, and year
        labels = []
        for value, rank, growth in zip(filtered_df['value'], filtered_df['rankings'], filtered_df['growth']):
            if indicator in ['Gross Domestic Product', 'State revenue']:
                label = f"{indicator}\n\n${int(value):,} {unit}\n\nGrowth: {growth:.2f}%"
            else:
                label = f"{indicator}\n\n{int(value):,} {unit}\n\nGrowth: {growth:.2f}%"
            labels.append(label)

        # Create a subplot at the specified position
        ax = fig.add_axes([positions[i][0], positions[i][1], sizes[i], sizes[i]])
        
        # Plot the pie chart with different colors for each pie
        colormaps = ['Pastel1', 'Pastel2', 'Accent', 'Paired']
        cmap = plt.cm.get_cmap(colormaps[i % len(colormaps)])
        wedges, texts = ax.pie(filtered_df['value'], startangle=140, colors=cmap(np.linspace(0, 1, len(filtered_df))))

        # Add labels at the center of each pie slice
        for j, wedge in enumerate(wedges):
            angle = (wedge.theta2 + wedge.theta1) 
            x = wedge.r * np.cos(angle * np.pi / 182)
            y = wedge.r * np.sin(angle * np.pi )
            ax.text(x, y, labels[j], horizontalalignment='center', verticalalignment='center', fontsize=16)

    # Adjust layout and save the plot to a BytesIO object
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the plot as a base64 string
    pie_charts_url = base64.b64encode(buf.getvalue()).decode('utf8')
    
    plt.close()
    
    return pie_charts_url


def generate_bar_charts(data):
     # Define the indicators to plot
    groups = ['E21', 'E22']

    # Create a figure with subplots
    fig, ax = plt.subplots(figsize=(4, 8))

    # Add a title for the whole chart
    fig.suptitle('Economic Indicators per Capita', fontsize=20)

    # Get the latest year with data available for the indicators
    latest_year = data['year'].max()

    # Filter the DataFrame for the selected indicators and latest year
    filtered_df = data[(data['group'].isin(groups)) & (data['year'] == latest_year)]

    # Pivot the DataFrame to get values for each state and indicator
    pivot_df = filtered_df.pivot(index='state', columns='group', values='value').reset_index()

    # Fill missing values with zeros
    pivot_df = pivot_df.fillna(0)

    # Print column names to verify
    print(pivot_df.columns)

    # Plot the grouped bar chart
    bar_width = 0.35
    index = np.arange(len(pivot_df))

    bar1 = ax.bar(index, pivot_df['E21'], bar_width, label='GDP per Capita', color='skyblue')
    bar2 = ax.bar(index + bar_width, pivot_df['E22'], bar_width, label='Income per Capita', color='lightgreen')

    ax.set_xlabel('State')
    ax.set_ylabel('Value')
    ax.set_title('Gross Domestic Product per Capita and Personal Income per Capita')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(pivot_df['state'], rotation=45)
    ax.legend()

    # Add labels on top of the bars
    for bar in bar1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f"${int(height):,}", ha='center', va='bottom', fontsize=10)
    for bar in bar2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f"${int(height):,}", ha='center', va='bottom', fontsize=10)

    # Adjust layout and save the plot to a BytesIO object
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the plot as a base64 string
    bar_charts_url = base64.b64encode(buf.getvalue()).decode('utf8')
    
    plt.close()
    
    return bar_charts_url