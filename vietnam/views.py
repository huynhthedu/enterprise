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
from .models import VnIndicators, VnData, VnProvince, VnGroup
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import urllib.parse
import matplotlib.ticker as ticker
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest



def calculations(year1, year2):
    
    # 1. create a dataframe     
    queryset = VnData.objects.filter(year=year1).values() | VnData.objects.filter(year=year2).values()
    
    # Convert QuerySet to a list of dictionaries
    data = list(queryset)

    # Create a DataFrame
    df = pd.DataFrame(data)    
    df = df.dropna()    
    
 
    # 3. Canculate new indicatiors by ratios of existing indicators and add to the dataframe
    new_groups = {
        ('E1302', 'E1105'): ('E1109'),
        ('E1208', 'E1207'): ('E1212'),        
    }

    new_rows = []
    for (group1, group2), (new_group_id) in new_groups.items():
        df_group1 = df[df['group'] == group1]
        df_group2 = df[df['group'] == group2]         
        
        if df_group1.empty or df_group2.empty:
            continue  # Skip if either group is empty
       
        merged_df = pd.merge(df_group1, df_group2, on=['id',  'year'], suffixes=('_1', '_2'))          
        
        if merged_df.empty:
            continue  # Skip if merge results in an empty DataFrame
        
        merged_df['value'] = merged_df.apply(
            lambda row: row['value_1'] / row['value_2']*100 if row['value_2'] != 0 else float('nan'), axis=1)
        
        for _, row in merged_df.iterrows():
            new_row = {
                'group': new_group_id,
                'id': row['id'],                
                'year': row['year'],
                'value': row['value']
            }
            new_rows.append(new_row)

    new_rows_df = pd.DataFrame(new_rows)
    df = pd.concat([df, new_rows_df], ignore_index=True)
    # df.loc[df['group'] == 'E66', 'value'] *= 100
    df.loc[df['group'].isin(['E1201', 'E1207', 'E1208', 'E1210', 'E1302', 'E1109']), 'value'] /= 1000    
    df.loc[df['group'].isin(['E1110', 'E1102', 'E1807']), 'value'] *= 100 

    # 4. Calculate growth between the two selected years for each indicator
    df = df.pivot_table(index=['group', 'id' ], columns='year', values='value').reset_index()
    
  
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
    # print(df)
    new_column_names = ['group', 'id', 'value1', 'value2', 'growth']
    df.columns = new_column_names
        
    # 5. caculate score for each indicator among states. The lowest value gets 1.0 and the highest get 7.0, the rankings
    indicators = VnIndicators.objects.all().values()
    indicators_df = pd.DataFrame(list(indicators))

    
    group_name = VnGroup.objects.all().values('id', 'name')
    province_name = VnProvince.objects.all().values('id', 'province')
    group_name_df = pd.DataFrame(list(group_name))
    province_name_df = pd.DataFrame(list(province_name))
    df = pd.merge(df, indicators_df, on=['group'])   
    df = pd.merge(df, province_name_df, on=['id'])        
    

    def calculate_scores(province_values, key_values):
        min_value = province_values.min()
        max_value = province_values.max()
        
        if min_value == max_value:
            return pd.Series([1] * len(province_values), index=province_values.index)  # Return a series of ones if all values are the same
        
        scores = pd.Series(index=province_values.index, dtype=float)
        
        for i in range(len(province_values)):
            if key_values.iloc[i] == 1:
                scores.iloc[i] = ((province_values.iloc[i] - min_value) / (max_value - min_value)) * 6 + 1
            elif key_values.iloc[i] == 0:
                scores.iloc[i] = 7 - ((province_values.iloc[i] - min_value) / (max_value - min_value)) * 6
        
        return scores

    # Eliminate empty or none values
    df = df.dropna()
    # print(df)
    # Drop specific rows
    # groups_to_drop = ['E65', 'E22', 'E24', 'E15']
    # df = df[~df['group'].isin(groups_to_drop)]    
    
    # try:
    #     df['score1'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value1'], x['status'])).reset_index(level=0, drop=True)
    #     df['score_gr'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['growth'], x['status'])).reset_index(level=0, drop=True)
    #     df['score2'] = df.groupby(['group']).apply(lambda x: calculate_scores(x['value2'], x['status'])).reset_index(level=0, drop=True)
    # except Exception as e:
    #     print("Error during groupby and apply operations:", e)    
    
    # df['rank1'] = df.groupby(['group'])['score1'].rank(method='min', ascending=False)
    # df['rankgr'] =df.groupby(['group'])['score_gr'].rank(method='min', ascending=False)
    # df['rank2'] = df.groupby(['group'])['score2'].rank(method='min', ascending=False)

    # Apply the calculate_scores function with the key field
    try:
        df['score1'] = df.groupby(['index']).apply(lambda x: calculate_scores(x['value1'], x['status'])).reset_index(level=0, drop=True)
        df['score_gr'] = df.groupby(['index']).apply(lambda x: calculate_scores(x['growth'], x['status'])).reset_index(level=0, drop=True)
        df['score2'] = df.groupby(['index']).apply(lambda x: calculate_scores(x['value2'], x['status'])).reset_index(level=0, drop=True)
    except Exception as e:
        print("Error during groupby and apply operations:", e)    
    
    df['rank1'] = df.groupby(['index'])['score1'].rank(method='min', ascending=False)
    df['rankgr'] =df.groupby(['index'])['score_gr'].rank(method='min', ascending=False)
    df['rank2'] = df.groupby(['index'])['score2'].rank(method='min', ascending=False)
    # print(df)
    # Sort by rank2
    # df = df[df['group'] == 'E1101']
    # df_sorted = df.sort_values(by='rank2')
    

    # # Print the sorted DataFrame
    # print(df_sorted)
    
    #6. Calculate weighted scores by groups of indicators, and overall then rankings 

    df['index'] = df['index'].str[:3]
    df['index_main'] = df['index'].str[:1]
    indicators_df['group_index'] = indicators_df['index'].str[:3]
    # df = pd.merge(df, indicators_df, on=['group'])
    df['weighted_score1'] = df['score1'] * df['weight']
    df['weighted_score_gr'] = df['score_gr'] * df['weight']
    df['weighted_score2'] = df['score2'] * df['weight']
    df['choice'] = df['index'].str[:2]
    df_com = df[df['choice'].isin(['E2'])]
    df = df[df['choice'].isin(['E1'])]
    # print(df)
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
        # Initialize variables to avoid UnboundLocalError
    # Economic Size and Development level
    weighted_avg_scores = pd.DataFrame()
    weighted_avg_scores_province = pd.DataFrame()
    # Calculate the overall weighted average score and growth score for each group and year
    try:
        weighted_avg_scores = df.groupby(['index', 'province']).apply(calculate_weighted_avg).reset_index()
        # print(weighted_avg_scores)
        weighted_avg_scores_province = df.groupby(['index_main', 'province']).apply(calculate_weighted_avg).reset_index()        
        # print(weighted_avg_scores_province)

        # Merge with group_name_df to get the names
        # weighted_avg_scores['group_prefix'] = weighted_avg_scores['group'].str[:3]
        # weighted_avg_scores = pd.merge(weighted_avg_scores, group_name_df, left_on='group_prefix', right_on='id')     
        # print(weighted_avg_scores)           
        weighted_avg_scores['weighted_rank1'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores['weighted_rank_gr'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores['weighted_rank2'] = weighted_avg_scores.groupby(['index'])['weighted_avg_score2'].rank(ascending=False)
        weighted_avg_scores_province['weighted_province_rank1'] = weighted_avg_scores_province.groupby(['index_main'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores_province['weighted_province_rank_gr'] = weighted_avg_scores_province.groupby(['index_main'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores_province['weighted_province_rank2'] = weighted_avg_scores_province.groupby(['index_main'])['weighted_avg_score2'].rank(ascending=False)

        weighted_avg_scores = pd.merge(weighted_avg_scores, group_name_df, left_on='index', right_on='id')     

    except Exception as e:
        print(f"An error occurred: {e}")
    df.loc[df['group'].isin(['E1201', 'E1207', 'E1208', 'E1210']), 'unit'] = 'Tỷ đồng'
    df.loc[df['group'].isin(['E1109']), 'unit'] = 'Phần trăm'
    df.loc[df['group'].isin(['E1302']), 'unit'] = 'Nghìn người'
    print(df)
    # print(weighted_avg_scores)
    # print(weighted_avg_scores_province)
    # Competitiveness    
    weighted_avg_scores_c = pd.DataFrame()
    weighted_avg_scores_province_c = pd.DataFrame()
    # Calculate the overall weighted average score and growth score for each group and year
    try:
        weighted_avg_scores_c = df_com.groupby(['index', 'province']).apply(calculate_weighted_avg).reset_index()
        # print(weighted_avg_scores)
        weighted_avg_scores_province_c = df_com.groupby(['index_main', 'province']).apply(calculate_weighted_avg).reset_index()        
        # print(weighted_avg_scores_province)

        # Merge with group_name_df to get the names
        # weighted_avg_scores['group_prefix'] = weighted_avg_scores['group'].str[:3]
        # weighted_avg_scores = pd.merge(weighted_avg_scores, group_name_df, left_on='group_prefix', right_on='id')     
        # print(weighted_avg_scores)           
        weighted_avg_scores_c['weighted_rank1'] = weighted_avg_scores_c.groupby(['index'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores_c['weighted_rank_gr'] = weighted_avg_scores_c.groupby(['index'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores_c['weighted_rank2'] = weighted_avg_scores_c.groupby(['index'])['weighted_avg_score2'].rank(ascending=False)
        weighted_avg_scores_province_c['weighted_province_rank1'] = weighted_avg_scores_province_c.groupby(['index_main'])['weighted_avg_score1'].rank(ascending=False)
        weighted_avg_scores_province_c['weighted_province_rank_gr'] = weighted_avg_scores_province_c.groupby(['index_main'])['weighted_avg_score_gr'].rank(ascending=False)
        weighted_avg_scores_province_c['weighted_province_rank2'] = weighted_avg_scores_province_c.groupby(['index_main'])['weighted_avg_score2'].rank(ascending=False)

        weighted_avg_scores_c = pd.merge(weighted_avg_scores_c, group_name_df, left_on='index', right_on='id')     

    except Exception as e:
        print(f"An error occurred: {e}")
    df_com.loc[df_com['group'].isin(['E1201', 'E1207', 'E1208', 'E1210']), 'unit'] = 'Tỷ đồng'
    df_com.loc[df_com['group'].isin(['E1109']), 'unit'] = 'Phần trăm'
    df_com.loc[df_com['group'].isin(['E1302']), 'unit'] = 'Nghìn người'
    # print(df_com)

    context = {
        'df': df,
        'weighted_avg_scores': weighted_avg_scores,
        'weighted_avg_scores_province': weighted_avg_scores_province,
        'df_com': df_com,
        'weighted_avg_scores_c': weighted_avg_scores_c,
        'weighted_avg_scores_province_c': weighted_avg_scores_province_c,
    }
    return context


def vietnam(request):
    # Fetch inputs
    provinces = VnProvince.objects.values_list('province', flat=True).distinct().order_by('province')
    years = list(range(2009, 2024))  # Valid years range
    indicators = list(VnIndicators.objects.filter(weight__gt=0).values_list('indicators', flat=True).distinct().order_by('group'))

    # Initialize variables
    selected_province = 'Bình Định'
    selected_indicators = ['GRDP', 'Dân số']
    year1 = 2019
    year2 = 2023
    warning_message = None

    if request.method == 'GET':
        # Fetch inputs with default values
        selected_province = request.GET.get('province', selected_province)
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
        if row['unit'] == 'Phần trăm':
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
    weighted_avg_scores_province = calculations_result['weighted_avg_scores_province']
    map_color = calculations_result['weighted_avg_scores_province']

    # Order the DataFrame by group
    df = df.sort_values(by='group')
    

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df = df[df['indicators'] == indicator].sort_values(by='value2', ascending=True)
        # print(indicator_df)
        # Skip plotting if indicator_df is empty
        if indicator_df.empty:
            print(f"No data available for indicator: {indicator}")
            continue

        # Create a new column combining state names and rank2 with no decimal
        indicator_df['province_rank'] = indicator_df.apply(lambda row: f"{row['province']} {int(row['rank2'])}", axis=1)
        
        bars = ax.barh(indicator_df['province_rank'], indicator_df['value2'], label=indicator)
        
       
    # Prepare context for rendering
    weighted_avg_scores_selected_province = weighted_avg_scores[weighted_avg_scores['province'] == selected_province]
    weighted_avg_scores_province_selected_province = weighted_avg_scores_province[weighted_avg_scores_province['province'] == selected_province]
    df_selected_province = df[df['province'] == selected_province]
    

    df_selected_province['value2'] = df_selected_province.apply(format_value, axis=1)
    # print(df_selected_province)
    # print(df_selected_province.columns)
    # print(weighted_avg_scores_selected_province)
    # print(weighted_avg_scores_province_selected_province)

    df1_dict = df_selected_province.to_dict(orient='records')
    # print(df1_dict)
    df2_dict = weighted_avg_scores_selected_province.to_dict(orient='records')
    df3_dict = weighted_avg_scores_province_selected_province.to_dict(orient='records')
    df4_dict = map_color.to_dict(orient='records')
    
    # Competiveness    
    calculations_result_c = calculations(year1, year2)
    df_com = calculations_result_c['df_com']
    weighted_avg_scores_c = calculations_result_c['weighted_avg_scores_c']
    weighted_avg_scores_province_c = calculations_result_c['weighted_avg_scores_province_c']
    map_color = calculations_result_c['weighted_avg_scores_province_c']

    # Order the DataFrame by group
    df_com = df_com.sort_values(by='group')
    

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df_c = df_com[df_com['indicators'] == indicator].sort_values(by='value2', ascending=True)
        # print(indicator_df)
        # Skip plotting if indicator_df is empty
        if indicator_df_c.empty:
            print(f"No data available for indicator: {indicator}")
            continue

        # Create a new column combining state names and rank2 with no decimal
        indicator_df_c['province_rank'] = indicator_df_c.apply(lambda row: f"{row['province']} {int(row['rank2'])}", axis=1)
        
        bars = ax.barh(indicator_df_c['province_rank'], indicator_df_c['value2'], label=indicator)
        
       
    # Prepare context for rendering
    weighted_avg_scores_selected_province_c = weighted_avg_scores_c[weighted_avg_scores_c['province'] == selected_province]
    weighted_avg_scores_province_selected_province_c = weighted_avg_scores_province_c[weighted_avg_scores_province_c['province'] == selected_province]
    df_selected_province_c = df_com[df_com['province'] == selected_province]
    

    df_selected_province_c['value2'] = df_selected_province_c.apply(format_value, axis=1)
    # print(df_selected_province)
    # print(df_selected_province.columns)
    # print(weighted_avg_scores_selected_province)
    # print(weighted_avg_scores_province_selected_province)

    df1_dict_c = df_selected_province_c.to_dict(orient='records')
    # print(df1_dict)
    df2_dict_c = weighted_avg_scores_selected_province_c.to_dict(orient='records')
    df3_dict_c = weighted_avg_scores_province_selected_province_c.to_dict(orient='records')
    df4_dict_c = map_color.to_dict(orient='records')
    
    context ={
        'df': df,
        'df1': df1_dict,
        'df2': df2_dict,
        'df3': df3_dict,
        'df_com': df_com,
        'df1_c': df1_dict_c,
        'df2_c': df2_dict_c,
        'df3_c': df3_dict_c,
        'provinces': provinces,
        'years': years,
        'db4': df4_dict,
        'indicators': indicators,
        'selected_indicators': selected_indicators,
        'selected_province': selected_province,
        'year1': year1,
        'year2': year2,
        'warning_message': warning_message, 
    }

    return render(request, 'vietnam/vietnam.html', context)

