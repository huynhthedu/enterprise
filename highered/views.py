from django.shortcuts import render
from data.models import C2023B, Hd2023, Ic2023Ay, RankingsIndicator, Effy2023, Adm2023
from django.db.models import Sum
import pandas as pd
import logging
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from django.db.models import IntegerField
from django.db.models.functions import Cast
import time
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
import base64


# Configure logging
logger = logging.getLogger(__name__)

def degree(request):
    institutions = list(Hd2023.objects.values_list('instnm', flat=True).distinct().order_by('unitid'))    
    chosen_institution = request.GET.get('instnm', 'Indiana University-Bloomington')
    institution_data = list(Hd2023.objects.values('instnm', 'unitid', 'stabbr').distinct())     
    institution_df = pd.DataFrame(institution_data)   

    if request.GET.get('query'):
        query = request.GET['query'].lower()
        suggestions = [inst for inst in institutions if query in inst.lower()]
        return JsonResponse({'suggestions': suggestions})

# I - Admission
    admission_data = list(Adm2023.objects.filter(year=2023).values())
    admission_data = pd.DataFrame(admission_data)
    admission_data['admission_rate'] = admission_data.apply(
        lambda row: (row['admssn'] / row['applcn'] * 100) if row['applcn'] != 0 else None,
        axis=1
    )
    admission_data['acceptance_rate'] = admission_data.apply(
        lambda row: (row['enrlt'] / row['admssn'] * 100) if row['admssn'] != 0 else None,
        axis=1
    )
    merged_admission = pd.merge(admission_data, institution_df, how='right', on='unitid')    
    merged_admission = merged_admission.sort_values(by='admission_rate')
    merged_admission = merged_admission[merged_admission['admission_rate'] > 0]
    merged_admission = merged_admission.loc[:, [ 'unitid', 'instnm', 'admission_rate', 'acceptance_rate', 'applcn', 'enrlt' ]]
    print(merged_admission.head())
    chosen_admisson = merged_admission[merged_admission['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    chosen_admisson = chosen_admisson.to_dict(orient='records')
    merged_admission = merged_admission.to_dict(orient='list')
    
    
    # Print a portion of the dictionary (first 3 entries for each key)
    portion = {key: value[:3] for key, value in merged_admission.items()}
    # print(portion)


# II - Student
    fields = [
        'unitid', 'cstotlt', 'cstotlm', 'cstotlw', 'csaiant', 'csaianm', 'csaianw', 'csasiat', 'csasiam',
        'csasiaw', 'csbkaat', 'csbkaam','csbkaaw', 'cshispt', 'cshispm', 'cshispw', 'csnhpit', 'csnhpim',
        'csnhpiw', 'cswhitt', 'cswhitm', 'cswhitw', 'cs2mort', 'cs2morm', 'cs2morw', 'csunknt','csunknm',
        'csunknw', 'csnralt', 'csnralm', 'csnralw'
    ]

    student_fields = ['unitid', 'effyalev', 'effylev', 'lstudy', 'efytotlt', 'efytotlm', 'efytotlw', 'efyaiant', 
     'efyaianm', 'efyaianw', 'efyasiat', 'efyasiam', 'efyasiaw', 'efybkaat', 'efybkaam', 'efybkaaw', 
     'efyhispt', 'efyhispm', 'efyhispw', 'efynhpit', 'efynhpim', 'efynhpiw', 'efywhitt', 'efywhitm', 
     'efywhitw', 'efy2mort', 'efy2morm', 'efy2morw', 'efyunknt', 'efyunknm', 'efyunknw', 'efynralt', 
     'efynralm', 'efynralw'
    ]

    student_choices = [
        ('efytotlt', 'Total'),        
        ('efyasiat', 'Asian'),
        ('efybkaat', 'Black'),
        ('efyhispt', 'Latino'),
        ('efynhpit', 'Islander'),
        ('efyaiant', 'Native'),
        ('efywhitt', 'White'),
        ('efynralt', 'Nonresident'),
        ('efy2mort', 'Two or more races'),
        ('efyunknt', 'Unknown'),
        
    ]

    CHOICES = [
        ('cstotlt', 'Total'),        
        ('csasiat', 'Asian'),
        ('csbkaat', 'Black'),
        ('cshispt', 'Latino'),
        ('csnhpit', 'Islander'),
        ('csaiant', 'Native'),
        ('cswhitt', 'White'),
        ('csnralt', 'Nonresident'),
        ('cs2mort', 'Two or more races'),
        ('csunknt', 'Unknown'),
        
    ]

    
    degree_data = list(C2023B.objects.values(*fields))
    student_data = list(Effy2023.objects.annotate(
    effyalev_int=Cast('effyalev', IntegerField())).filter(effyalev_int=1).values(*student_fields))
    # print(len(student_data))

    
    degree_df = pd.DataFrame(degree_data)
    student_df = pd.DataFrame(student_data)
    # print(degree_df.head())

    merged_data = pd.merge(degree_df, institution_df, how='right', on='unitid')    
    merged_all = pd.merge(merged_data, student_df, how='left', on='unitid')    
    chosen_value = merged_all[merged_all['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    # print(chosen_value.head())

    # Structure the data for the table
    table_data = []
    for key, choice in CHOICES:
        if key in chosen_value.columns:
            men_key = key[:-1] + 'm'  # Replace the last character with 'm'
            women_key = key[:-1] + 'w'  # Replace the last character with 'w'
            total_value = chosen_value[key].values[0] if key in chosen_value.columns else None
            men_value = chosen_value[men_key].values[0] if men_key in chosen_value.columns else None
            women_value = chosen_value[women_key].values[0] if women_key in chosen_value.columns else None

            table_data.append({
                'choice': choice,
                'total_a': total_value,
                'men_a': men_value,
                'women_a': women_value,
            })

    table_student = []
    for key, choice in student_choices:
        if key in chosen_value.columns:
            men_key = key[:-1] + 'm'  # Replace the last character with 'm'
            women_key = key[:-1] + 'w'  # Replace the last character with 'w'
            total_value = chosen_value[key].values[0] if key in chosen_value.columns else None
            men_value = chosen_value[men_key].values[0] if men_key in chosen_value.columns else None
            women_value = chosen_value[women_key].values[0] if women_key in chosen_value.columns else None


            table_student.append({
                'choice': choice,
                'total_s': total_value,
                'men_s': men_value,
                'women_s': women_value,
            })

    table_data = pd.DataFrame(table_data)
    table_student =pd.DataFrame(table_student)
    merged_table = pd.merge(table_data, table_student, how='outer', on ='choice')
    merged_table['student'] = merged_table.apply(lambda row: (row['total_s'] - row['total_a']), axis=1)
    merged_table['men'] = merged_table.apply(lambda row: (row['men_s'] - row['men_a']), axis=1)
    merged_table['women'] = merged_table.apply(lambda row: (row['women_s'] - row['women_a']), axis=1)
    merged_table = merged_table.sort_values(by ='choice', ascending=False)                                             
    students = merged_table[merged_table['choice'] == 'Total']
    students = students.to_dict(orient='records')
    students_portfolio = merged_table[merged_table['choice'] != 'Total']

    # Sutdent graph

    fig, ax = plt.subplots()
    ax.pie(students_portfolio['student'], labels=students_portfolio['choice'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Save the chart to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode the image to base64
    image_students = base64.b64encode(buffer.read()).decode('utf-8')

    #  Degree graph
    fig, ax = plt.subplots()

    ax.pie(students_portfolio['total_a'], labels=students_portfolio['choice'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Save the chart to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode the image to base64
    image_degree = base64.b64encode(buffer.read()).decode('utf-8')


    # print(students)
    merged_table = merged_table.to_dict(orient='records')


    # -------------------

    tuition_fields = [
        'unitid',
        'chg2ay1', 'chg2ay2', 'chg2ay3', 'chg2at1', 'chg2at2', 'chg2at3',
        'chg2af1', 'chg2af2', 'chg2af3', 'chg3ay1', 'chg3ay2', 'chg3ay3',
        'chg3at1', 'chg3at2', 'chg3at3', 'chg3af1', 'chg3af2', 'chg3af3',
        'chg4ay1', 'chg4ay2', 'chg4ay3', 'chg5ay1', 'chg5ay2', 'chg5ay3',
        'chg6ay1', 'chg6ay2', 'chg6ay3', 'chg7ay1', 'chg7ay2', 'chg7ay3',
        'chg8ay1', 'chg8ay2', 'chg8ay3', 'chg9ay1', 'chg9ay2', 'chg9ay3'
    ]

    tuition_choices = {
        "chg2ay": "In-state tuition and fees",
        "chg2at": "In-state tuition",
        "chg2af": "In-state fees",
        "chg3ay": "Out-of-state tuition and fees",
        "chg3at": "Out-of-state tuition",
        "chg3af": "Out-of-state fees",
        "chg4ay": "Books and supplies",
        "chg5ay": "On campus, room and board",
        "chg6ay": "On campus, other expenses",
        "chg7ay": "Off campus (not with family), room and board",
        "chg8ay": "Off campus (not with family), other expenses",
        "chg9ay": "Off campus (with family), other expenses"
    }

    
    tuition_data = list(Ic2023Ay.objects.values(*tuition_fields))
    income_per_capita = list(RankingsIndicator.objects.filter(year=2023, indicator='Personal Income per Capita').values('stabbr', 'value').distinct())    
    
    income_df = pd.DataFrame(income_per_capita)
    income_df = income_df.rename(columns={'value': 'income_pc'})    
    institution_df = pd.merge(institution_df, income_df, how='left', on='stabbr')    
    degree_df = pd.DataFrame(tuition_data)
    merged_tuition = pd.merge(degree_df, institution_df, how='right', on='unitid')
    merged_tuition ['chg2ay3'] = pd.to_numeric(merged_tuition ['chg2ay3'])
    merged_tuition['rankings_tuition'] = merged_tuition['chg2ay3'].rank(ascending=False)
    top10_rankings = merged_tuition.nlargest(10, 'chg2ay3' )
    lowest10_rankings = merged_tuition.nsmallest(10, 'chg2ay3' )
    merged_tuition = merged_tuition[merged_tuition['instnm'] == chosen_institution]        

    # Pivot the data
    table_tuition = []
    for _, row in merged_tuition.iterrows():
        unitid = row['unitid']
        for year in ['1', '2', '3']:
            table_tuition.append({
                'unitid': unitid,
                'instnm': row['instnm'],
                'income_pc': row['income_pc'],
                'rankings_tuition': row['rankings_tuition'],
                'year': f'2020-2{year}',
                'chg2ay': row[f'chg2ay{year}'],
                'chg2at': row[f'chg2at{year}'],
                'chg2af': row[f'chg2af{year}'],
                'chg3ay': row[f'chg3ay{year}'],
                'chg3at': row[f'chg3at{year}'],
                'chg3af': row[f'chg3af{year}'],
                'chg4ay': row[f'chg4ay{year}'],
                'chg5ay': row[f'chg5ay{year}'],
                'chg6ay': row[f'chg6ay{year}'],
                'chg7ay': row[f'chg7ay{year}'],
                'chg8ay': row[f'chg8ay{year}'],
                'chg9ay': row[f'chg9ay{year}']
            })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(table_tuition)    

    # Melt the DataFrame to have years as columns
    melted_df = df.melt(id_vars=['unitid', 'year', 'instnm', 'income_pc', 'rankings_tuition'], var_name='item', value_name='value')

    # Pivot the DataFrame to have years as columns
    pivoted_df = melted_df.pivot_table(index=['unitid', 'instnm', 'item', 'income_pc', 'rankings_tuition' ], columns='year', values='value').reset_index()

    # Rename the columns
    pivoted_df.columns.name = None
    pivoted_df.columns = ['unitid', 'instnm', 'item', 'income_pc', 'rankings_tuition', "y2021", "y2022", "y2023" ]

    # Calculate the growth between years with condition to avoid divide by zero
    pivoted_df['gr22'] = pivoted_df.apply(
        lambda row: ((row['y2022'] - row['y2021']) / row['y2021'] * 100) if row['y2021'] != 0 else None,
        axis=1
    )
    pivoted_df['gr23'] = pivoted_df.apply(
        lambda row: ((row['y2023'] - row['y2022']) / row['y2022'] * 100) if row['y2022'] != 0 else None,
        axis=1
    )

    pivoted_df['to_ic'] = pivoted_df.apply(
        lambda row: ((row['y2023'] ) / row['income_pc'] * 100) if row['income_pc'] != 0 else None,
        axis=1
    )


    # Map the item names to their descriptions
    pivoted_df['item'] = pivoted_df['item'].map(tuition_choices)

    order = ["In-state tuition and fees", "In-state tuition", 
             "In-state fees", "Out-of-state tuition and fees", 
             "Out-of-state tuition", "Out-of-state fees", 
             "Books and supplies", "On campus, room and board", 
             "On campus, other expenses", 
             "Off campus (not with family), room and board", 
             "Off campus (not with family), other expenses", 
             "Off campus (with family), other expenses"]
    pivoted_df['item'] = pd.Categorical(pivoted_df['item'], categories=order, ordered=True)
    
    # pivoted_df['rankings_tuition'] = pivoted_df.groupby('item')['y2023'].rank(ascending=False)   

    pivoted_df = pivoted_df.sort_values('item')
    # print(pivoted_df.head())
    # pivoted_df = pivoted_df[pivoted_df['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    tuition = pivoted_df[(pivoted_df['instnm'] == chosen_institution) & (pivoted_df['item'] == 'In-state tuition and fees')] if chosen_institution else pd.DataFrame()
    tuition_structure = pivoted_df[
    (pivoted_df['instnm'] == chosen_institution) & 
    ((pivoted_df['item'] == 'Out-of-state tuition') | 
     (pivoted_df['item'] == 'In-state tuition') | 
     (pivoted_df['item'] == 'On campus, room and board') | 
     (pivoted_df['item'] == 'Books and supplies') |      
     (pivoted_df['item'] == 'On campus, other expenses'))
    ] if chosen_institution else pd.DataFrame()
    # print(tuition)

     # Cost by years

    cost_structure = tuition_structure[['item', 'y2021', 'y2022', 'y2023']]
    cost_structure.rename(columns={'y2021': '2021', 'y2022': '2022', 'y2023': '2023'}, inplace=True)
    chart_data = cost_structure.to_dict(orient='list')
    print(chart_data)
    

    cost_structure.set_index('item', inplace=True)

    # Plot the bar chart with categories by year
    plt.figure(figsize=(24, 6)) 
    cost_structure.T.plot(kind='bar')
    plt.title('Tuition Structure by Year')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.xticks(rotation=0)
    plt.legend(title='Category')

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_cost = base64.b64encode(buffer.read()).decode('utf-8')
     
     #  Tutition Structure graph
    fig, ax = plt.subplots()

    ax.pie(tuition_structure['y2023'], labels=tuition_structure['item'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Save the chart to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode the image to base64
    image_tuition = base64.b64encode(buffer.read()).decode('utf-8')
    # print(pivoted_df.head())
    pivot_data = pivoted_df.to_dict(orient='records')
    top10 = top10_rankings.to_dict(orient='records')
    tuition = tuition.to_dict(orient='records')
    lowest10 = lowest10_rankings.to_dict(orient='records')


    context = {
        'table_data': merged_table,    
        'students'  : students,
        'table_tuition': table_tuition,
        'tuition': tuition,
        'top10': top10,
        'lowest10': lowest10,
        'pivot_data': pivot_data,
        'institutions': institutions,
        'chosen_institution': chosen_institution,
        'CHOICES': CHOICES,
        'image_students': image_students,
        'image_degree': image_degree,
        'image_tuition': image_tuition,
        'image_cost': image_cost,
        'chart_data':chart_data,
        'chosen_admission': chosen_admisson,
        'merged_admission': merged_admission,

    }

    return render(request, 'highered/degree.html', context)



def tuition(request):
    institutions = list(Hd2023.objects.values_list('instnm', flat=True).distinct().order_by('unitid'))
    chosen_institution = request.GET.get('instnm') or (institutions[0] if institutions else None)

    if request.GET.get('query'):
        query = request.GET['query'].lower()
        suggestions = [inst for inst in institutions if query in inst.lower()]
        return JsonResponse({'suggestions': suggestions})

    fields = [
        'unitid',
        'chg2ay1', 'chg2ay2', 'chg2ay3', 'chg2at1', 'chg2at2', 'chg2at3',
        'chg2af1', 'chg2af2', 'chg2af3', 'chg3ay1', 'chg3ay2', 'chg3ay3',
        'chg3at1', 'chg3at2', 'chg3at3', 'chg3af1', 'chg3af2', 'chg3af3',
        'chg4ay1', 'chg4ay2', 'chg4ay3', 'chg5ay1', 'chg5ay2', 'chg5ay3',
        'chg6ay1', 'chg6ay2', 'chg6ay3', 'chg7ay1', 'chg7ay2', 'chg7ay3',
        'chg8ay1', 'chg8ay2', 'chg8ay3', 'chg9ay1', 'chg9ay2', 'chg9ay3'
    ]

    CHOICES = {
        "chg2ay": "In-state tuition and fees",
        "chg2at": "In-state tuition",
        "chg2af": "In-state fees",
        "chg3ay": "Out-of-state tuition and fees",
        "chg3at": "Out-of-state tuition",
        "chg3af": "Out-of-state fees",
        "chg4ay": "Books and supplies",
        "chg5ay": "On campus, room and board",
        "chg6ay": "On campus, other expenses",
        "chg7ay": "Off campus (not with family), room and board",
        "chg8ay": "Off campus (not with family), other expenses",
        "chg9ay": "Off campus (with family), other expenses"
    }

    institution_data = list(Hd2023.objects.values('instnm', 'unitid', 'latitude', 'longitud', 'stabbr').distinct())
    tuition_data = list(Ic2023Ay.objects.values(*fields))
    income_per_capita = list(RankingsIndicator.objects.filter(year=2023, indicator='Personal Income per Capita').values('stabbr', 'value'))
    # print(income_per_capita)
    
    income_df = pd.DataFrame(income_per_capita)
    income_df = income_df.rename(columns={'value': 'income_pc'})
    # print(income_df.head())
    institution_dframe = pd.DataFrame(institution_data)
    institution_df = pd.merge(institution_dframe, income_df, how='left', on='stabbr')
    # print(institution_df.head())
    degree_df = pd.DataFrame(tuition_data)

    merged_data = pd.merge(degree_df, institution_df, how='right', on='unitid')

    # Pivot the data
    table_data = []
    for _, row in merged_data.iterrows():
        unitid = row['unitid']
        for year in ['1', '2', '3']:
            table_data.append({
                'unitid': unitid,
                'instnm': row['instnm'],
                'income_pc': row['income_pc'],
                'year': f'2020-2{year}',
                'chg2ay': row[f'chg2ay{year}'],
                'chg2at': row[f'chg2at{year}'],
                'chg2af': row[f'chg2af{year}'],
                'chg3ay': row[f'chg3ay{year}'],
                'chg3at': row[f'chg3at{year}'],
                'chg3af': row[f'chg3af{year}'],
                'chg4ay': row[f'chg4ay{year}'],
                'chg5ay': row[f'chg5ay{year}'],
                'chg6ay': row[f'chg6ay{year}'],
                'chg7ay': row[f'chg7ay{year}'],
                'chg8ay': row[f'chg8ay{year}'],
                'chg9ay': row[f'chg9ay{year}']
            })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(table_data)
    # print(df.head())

    # Melt the DataFrame to have years as columns
    melted_df = df.melt(id_vars=['unitid', 'year', 'instnm', 'income_pc'], var_name='item', value_name='value')

    # Pivot the DataFrame to have years as columns
    pivoted_df = melted_df.pivot_table(index=['unitid', 'instnm', 'item', 'income_pc' ], columns='year', values='value').reset_index()

    # Rename the columns
    pivoted_df.columns.name = None
    pivoted_df.columns = ['unitid', 'instnm', 'item', 'income_pc', "y2021", "y2022", "y2023" ]

    # Calculate the growth between years with condition to avoid divide by zero
    pivoted_df['gr22'] = pivoted_df.apply(
        lambda row: ((row['y2022'] - row['y2021']) / row['y2021'] * 100) if row['y2021'] != 0 else None,
        axis=1
    )
    pivoted_df['gr23'] = pivoted_df.apply(
        lambda row: ((row['y2023'] - row['y2022']) / row['y2022'] * 100) if row['y2022'] != 0 else None,
        axis=1
    )

    pivoted_df['to_ic'] = pivoted_df.apply(
        lambda row: ((row['y2023'] ) / row['income_pc'] * 100) if row['income_pc'] != 0 else None,
        axis=1
    )


    # Map the item names to their descriptions
    pivoted_df['item'] = pivoted_df['item'].map(CHOICES)

    order = ["In-state tuition and fees", "In-state tuition", 
             "In-state fees", "Out-of-state tuition and fees", 
             "Out-of-state tuition", "Out-of-state fees", 
             "Books and supplies", "On campus, room and board", 
             "On campus, other expenses", 
             "Off campus (not with family), room and board", 
             "Off campus (not with family), other expenses", 
             "Off campus (with family), other expenses"]
    pivoted_df['item'] = pd.Categorical(pivoted_df['item'], categories=order, ordered=True)
    pivoted_df['y2023'] = pd.to_numeric(pivoted_df['y2023'])
    pivoted_df['rankings_tuition'] = pivoted_df.groupby('item')['y2023'].rank(ascending=False)
    top10_rankings = pivoted_df.groupby('item').apply(lambda x: x.nlargest(10, 'y2023')).reset_index(drop=True)
    top10_rankings = top10_rankings[top10_rankings['item'] == 'In-state tuition and fees']
    lowest10_rankings = pivoted_df.groupby('item').apply(lambda x: x.nsmallest(10, 'y2023')).reset_index(drop=True)
    lowest10_rankings = lowest10_rankings[lowest10_rankings['item'] == 'In-state tuition and fees']
    pivoted_df = pivoted_df.sort_values('item')
    # print(pivoted_df.head())
    pivoted_df = pivoted_df[pivoted_df['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    tuition = pivoted_df[(pivoted_df['instnm'] == chosen_institution) & (pivoted_df['item'] == 'In-state tuition and fees')] if chosen_institution else pd.DataFrame()
    # print(tuition)

    # print(pivoted_df.head())
    pivot_data = pivoted_df.to_dict(orient='records')
    top10 = top10_rankings.to_dict(orient='records')
    tuition = tuition.to_dict(orient='records')
    lowest10 = lowest10_rankings.to_dict(orient='records')
  
    chosen = Hd2023.objects.filter(instnm=chosen_institution).values_list('unitid', flat=True)
    chosen = Hd2023.objects.get(instnm=chosen_institution).unitid
    print(chosen)
    student_data = students()
    student_data = student_data['table_data']
    student_data = student_data.to_dict(orient='records')
    # student_data = student_data[student_data['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    # filtered_data = [record for record in student_data if record['student'] > 0]
    # null_count= student_data['unitid'].isnull().sum()
    # print(filtered_data)
    # print(student_data.head())
    # student_data = student_data.loc[(student_data['unitid'] == chosen) & (student_data['unitid'].notnull())]    
    

    context = {
        'table_data': table_data,
        'tuition': tuition,
        'top10': top10,
        'lowest10': lowest10,
        'pivot_data': pivot_data,
        'institutions': institutions,
        'chosen_institution': chosen_institution,
        'CHOICES': CHOICES,
        # 'income_df': income_df.to_html()  # Convert DataFrame to HTML
    }

    return render(request, 'highered/tuition.html', context)


def tuition_income(request):
    institutions = list(Hd2023.objects.values_list('instnm', flat=True).distinct().order_by('unitid'))
    chosen_institution = request.GET.get('instnm') or (institutions[0] if institutions else None)

    if request.GET.get('query'):
        query = request.GET['query'].lower()
        suggestions = [inst for inst in institutions if query in inst.lower()]
        return JsonResponse({'suggestions': suggestions})

    # Ensure university_id is passed correctly
    university_id = request.GET.get('university_id')
    if not university_id:
        return JsonResponse({'error': 'university_id is required'}, status=400)

    try:
        university = Hd2023.objects.get(unitid=university_id)  # Query using unitid
    except Hd2023.DoesNotExist:
        return JsonResponse({'error': 'University not found'}, status=404)

    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.reverse((university.latitude, university.longitude), exactly_one=True)
    state = location.raw['address']['state']
    
    # Query the RankingIndicator model
    try:
        ranking_indicator = RankingsIndicator.objects.get(state=state, year=2023, indicator='Personal Income per Capita')
        income_per_capita = ranking_indicator.value
    except RankingsIndicator.DoesNotExist:
        income_per_capita = None

    # Create a DataFrame
    data = {
        'unitid': [university.unitid],
        'instnm': [university.instnm],
        'income_pc': [income_per_capita]
    }
    final_df = pd.DataFrame(data)
    # print(final_df.head())
    student_data = students()
    table_data = student_data['table_data']
    print(table_data.head())

    context = {
        'data': final_df.to_html(),  # Convert DataFrame to HTML
        'institutions': institutions,
        'chosen_institution': chosen_institution,
    }

    return render(request, 'highered/tuition.html', context)



def student(request):
    institutions = list(Hd2023.objects.values_list('instnm', flat=True).distinct().order_by('unitid'))
    chosen_institution = request.GET.get('instnm') or (institutions[0] if institutions else None)

    if request.GET.get('query'):
        query = request.GET['query'].lower()
        suggestions = [inst for inst in institutions if query in inst.lower()]
        return JsonResponse({'suggestions': suggestions})

    fields = [
        'unitid',
        'cstotlt',
        'cstotlm',
        'cstotlw',
        'csaiant',
        'csaianm',
        'csaianw',
        'csasiat',
        'csasiam',
        'csasiaw',
        'csbkaat',
        'csbkaam',
        'csbkaaw',
        'cshispt',
        'cshispm',
        'cshispw',
        'csnhpit',
        'csnhpim',
        'csnhpiw',
        'cswhitt',
        'cswhitm',
        'cswhitw',
        'cs2mort',
        'cs2morm',
        'cs2morw',
        'csunknt',
        'csunknm',
        'csunknw',
        'csnralt',
        'csnralm',
        'csnralw'
    ]

    CHOICES = [
        ('cstotlt', 'Total'),        
        ('csasiat', 'Asian'),
        ('csbkaat', 'Black'),
        ('cshispt', 'Latino'),
        ('csnhpit', 'Islander'),
        ('csaiant', 'Native'),
        ('cswhitt', 'White'),
        ('csnralt', 'Nonresident'),
        ('cs2mort', 'Two or more races'),
        ('csunknt', 'Unknown'),
        
    ]

    institution_data = list(Hd2023.objects.values('instnm', 'unitid').distinct())
    degree_data = list(C2023B.objects.values(*fields))

    institution_df = pd.DataFrame(institution_data)
    degree_df = pd.DataFrame(degree_data)
    print(degree_df.head())

    merged_data = pd.merge(degree_df, institution_df, how='left', on='unitid')
    chosen_value = merged_data[merged_data['instnm'] == chosen_institution] if chosen_institution else pd.DataFrame()
    chosen_value_dict = chosen_value.to_dict(orient='records')

    # Structure the data for the table
    table_data = []
    for key, choice in CHOICES:
        if key in chosen_value.columns:
            men_key = key[:-1] + 'm'  # Replace the last character with 'm'
            women_key = key[:-1] + 'w'  # Replace the last character with 'w'
            total_value = chosen_value[key].values[0] if key in chosen_value.columns else None
            men_value = chosen_value[men_key].values[0] if men_key in chosen_value.columns else None
            women_value = chosen_value[women_key].values[0] if women_key in chosen_value.columns else None

            # Debugging output
            # print(f"Key: {key}, Choice: {choice}")
            # print(f"Total: {total_value}, Men Key: {men_key}, Men: {men_value}, Women Key: {women_key}, Women: {women_value}")

            table_data.append({
                'choice': choice,
                'total': total_value,
                'men': men_value,
                'women': women_value,
            })

    context = {
        'table_data': table_data,
        'institutions': institutions,
        'chosen_institution': chosen_institution,
    }

    return render(request, 'highered/degree.html', context)


def students():
    institutions = list(Hd2023.objects.values_list('instnm', flat=True).distinct().order_by('unitid'))

    fields = [
        'unitid', 'cstotlt', 'cstotlm', 'cstotlw', 'csaiant', 'csaianm', 'csaianw', 'csasiat', 'csasiam',
        'csasiaw', 'csbkaat', 'csbkaam','csbkaaw', 'cshispt', 'cshispm', 'cshispw', 'csnhpit', 'csnhpim',
        'csnhpiw', 'cswhitt', 'cswhitm', 'cswhitw', 'cs2mort', 'cs2morm', 'cs2morw', 'csunknt','csunknm',
        'csunknw', 'csnralt', 'csnralm', 'csnralw'
    ]

    student_fields = ['unitid', 'effyalev', 'effylev', 'lstudy', 'efytotlt', 'efytotlm', 'efytotlw', 'efyaiant', 
     'efyaianm', 'efyaianw', 'efyasiat', 'efyasiam', 'efyasiaw', 'efybkaat', 'efybkaam', 'efybkaaw', 
     'efyhispt', 'efyhispm', 'efyhispw', 'efynhpit', 'efynhpim', 'efynhpiw', 'efywhitt', 'efywhitm', 
     'efywhitw', 'efy2mort', 'efy2morm', 'efy2morw', 'efyunknt', 'efyunknm', 'efyunknw', 'efynralt', 
     'efynralm', 'efynralw'
    ]

    student_choices = [
        ('efytotlt', 'Total'),        
        ('efyasiat', 'Asian'),
        ('efybkaat', 'Black'),
        ('efyhispt', 'Latino'),
        ('efynhpit', 'Islander'),
        ('efyaiant', 'Native'),
        ('efywhitt', 'White'),
        ('efynralt', 'Nonresident'),
        ('efy2mort', 'Two or more races'),
        ('efyunknt', 'Unknown'),
        
    ]

    CHOICES = [
        ('cstotlt', 'Total'),        
        ('csasiat', 'Asian'),
        ('csbkaat', 'Black'),
        ('cshispt', 'Latino'),
        ('csnhpit', 'Islander'),
        ('csaiant', 'Native'),
        ('cswhitt', 'White'),
        ('csnralt', 'Nonresident'),
        ('cs2mort', 'Two or more races'),
        ('csunknt', 'Unknown'),
        
    ]

    institution_data = list(Hd2023.objects.values('instnm', 'unitid').distinct())
    degree_data = list(C2023B.objects.values(*fields))
    student_data = list(Effy2023.objects.annotate(
    effyalev_int = Cast('effyalev', IntegerField())).filter(effyalev_int=1).values(*student_fields))
    print(len(student_data), len(institution_data))

    institution_df = pd.DataFrame(institution_data)
    degree_df = pd.DataFrame(degree_data)
    student_df = pd.DataFrame(student_data)
    # print(degree_df.head())

    merged_data = pd.merge(degree_df, institution_df, how='right', on='unitid')
    merged_all = pd.merge(merged_data, student_df, how='left', on='unitid')


    # Structure the data for the table
    table_data = []
    for key, choice in CHOICES:
        if key in merged_all.columns:
            men_key = key[:-1] + 'm'  # Replace the last character with 'm'
            women_key = key[:-1] + 'w'  # Replace the last character with 'w'
            total_value = merged_all[key].values[0] if key in merged_all.columns else None
            men_value = merged_all[men_key].values[0] if men_key in merged_all.columns else None
            women_value = merged_all[women_key].values[0] if women_key in merged_all.columns else None
            unitid = merged_all['unitid']
            instnm = merged_all['instnm']

            table_data.append({
                'unitid': unitid,
                'instnm': instnm,
                'choice': choice,
                'total_a': total_value,
                'men_a': men_value,
                'women_a': women_value,
            })

    table_student = []
    for key, choice in student_choices:
        if key in merged_all.columns:
            men_key = key[:-1] + 'm'  # Replace the last character with 'm'
            women_key = key[:-1] + 'w'  # Replace the last character with 'w'
            total_value = merged_all[key].values[0] if key in merged_all.columns else None
            men_value = merged_all[men_key].values[0] if men_key in merged_all.columns else None
            women_value = merged_all[women_key].values[0] if women_key in merged_all.columns else None


            table_student.append({
                'choice': choice,
                'total_s': total_value,
                'men_s': men_value,
                'women_s': women_value,
            })

    table_data = pd.DataFrame(table_data)
    table_student =pd.DataFrame(table_student)
    merged_table = pd.merge(table_data, table_student, how='outer', on ='choice')
    merged_table['student'] = merged_table.apply(lambda row: (row['total_s'] - row['total_a']), axis=1)
    merged_table['men'] = merged_table.apply(lambda row: (row['men_s'] - row['men_a']), axis=1)
    merged_table['women'] = merged_table.apply(lambda row: (row['women_s'] - row['women_a']), axis=1)
    merged_table = merged_table.sort_values(by ='student', ascending=False)                                       

    # merged_table = merged_table.to_dict(orient='records')

    context = {
        'table_data': merged_table,
        'institutions': institutions,        
    }

    return  context

def check_error(request):

    student_data = students()
    student_data = student_data['table_data']
    print(student_data.head())
    # student_data = student_data.loc[(student_data['unitid'] == '151351') & (student_data['unitid'].notnull())]    
    

    context = {
        'table_data': student_data,
        'tuition': tuition,
    }

    return render(request, 'highered/error.html', context)
