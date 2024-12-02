import pandas as pd
import requests
from django.shortcuts import render

def fetch_excel_data():
    url = "https://docs.google.com/spreadsheets/d/1Xh3os9HEsu0E2XQbXXJHb6Rl5Gdr7SSd/export?format=xlsx"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return pd.read_excel(response.content)
    except Exception as e:
        print(f"Error: {e}")
        return None

def dashboard(request):
    data = fetch_excel_data()
    if data is None:
        return render(request, 'dashboard/error.html', {'message': 'Unable to fetch data.'})

    rank_columns = ['Rank_2010', 'Rank_Growth_2010_2019', 'Rank_2019', 'Rank_Growth_2019_2023', 'Rank_2023']
    for col in rank_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    def rank_color_class(rank):
        if pd.isna(rank):
            return 'rank-default'
        rank = int(rank)
        if 1 <= rank <= 10: return 'rank-green'
        if 11 <= rank <= 20: return 'rank-light-green'
        if 21 <= rank <= 30: return 'rank-yellow'
        if 31 <= rank <= 40: return 'rank-orange'
        if 41 <= rank <= 51: return 'rank-red'
        return 'rank-default'

    for col in rank_columns:
        data[f'{col}_color'] = data[col].apply(rank_color_class)

    states = data['State'].unique().tolist()
    selected_state = request.GET.get('state', 'All States')
    if selected_state != 'All States':
        data = data[data['State'] == selected_state]

    return render(request, 'dashboard/dashboard.html', {
        'table_data': data.to_dict(orient='records'),
        'columns': data.columns.tolist(),
        'states': states,
        'selected_state': selected_state,
    })
