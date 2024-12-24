from django.shortcuts import render
from rankings.views import calculations
import json

def home(request):
    selected_indicators = 'Gross Domestic Product'  # Default indicator
    selected_state = 'Indiana'  # Default state
    year1 = 2019  # Default year1
    year2 = 2023  # Default year2

    calculations_result = calculations(year1, year2)
    map_color = calculations_result['weighted_avg_scores_state']

    df1_dict = map_color.to_dict(orient='records')

    # Load GeoJSON data with coordinates
    with open('static/js/us-states.json') as f:
        geojson_data = json.load(f)

    # Merge ranking and score data with GeoJSON
    for feature in geojson_data['features']:
        state_name = feature['properties']['name']
        for state in df1_dict:
            if state['state'] == state_name:
                feature['properties']['rank'] = state['weighted_state_rank2']
                feature['properties']['score'] = state['weighted_avg_score2']
                break
    # print(geojson_data)
    context = {
        'geojson_data': json.dumps(geojson_data),
        'selected_indicators': selected_indicators,
        'selected_state': selected_state,
        'year1': year1,
        'year2': year2,
    }
    return render(request, 'homepage/home.html', context)