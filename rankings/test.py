from django.shortcuts import render
from .models import Indicator
from django.db.models import F, ExpressionWrapper, FloatField
import pandas as pd

def calculate_growth_and_rankings(request):
    states = Indicator.objects.values_list('state', flat=True).distinct()
    years = list(range(1998, 2024))

    if request.method == 'GET' and 'state' in request.GET and 'year1' in request.GET and 'year2' in request.GET:
        selected_state = request.GET['state']
        year1 = int(request.GET['year1'])
        year2 = int(request.GET['year2'])

        # Get data for selected state and years
        indicators = Indicator.objects.filter(state=selected_state, year__in=[year1, year2])

        # Debugging: print the retrieved indicators
        print(f"Indicators for state {selected_state} in years {year1} and {year2}: {indicators}")

        # Initialize dictionaries for growth and rankings
        growth_data = {}
        rankings_data = []

        for indicator in indicators:
            # Get the values for the two years
            year1_indicator = indicators.filter(indicator=indicator.indicator, year=year1).first()
            year2_indicator = indicators.filter(indicator=indicator.indicator, year=year2).first()

            # Debugging: Check if data for both years exists
            print(f"Year 1 Indicator: {year1_indicator}, Year 2 Indicator: {year2_indicator}")

            if year1_indicator and year2_indicator:
                year1_value = year1_indicator.value
                year2_value = year2_indicator.value

                # Debugging: Check values for the two years
                print(f"Year 1 Value: {year1_value}, Year 2 Value: {year2_value}")

                # If either value is None, skip this indicator
                if year1_value is None or year2_value is None:
                    print(f"Skipping {indicator.indicator} due to missing values.")
                    continue

                # Calculate growth
                growth = (year2_value - year1_value) / year1_value * 100 if year1_value != 0 else 0
                growth_data[indicator.indicator] = growth

                # Calculate rankings for year1, year2, and growth
                year1_rank = Indicator.objects.filter(year=year1).values('indicator', 'value').order_by('-value')
                year2_rank = Indicator.objects.filter(year=year2).values('indicator', 'value').order_by('-value')
                growth_rank = sorted(growth_data.items(), key=lambda x: x[1], reverse=True)

                year1_rankings = {item['indicator']: index+1 for index, item in enumerate(year1_rank)}
                year2_rankings = {item['indicator']: index+1 for index, item in enumerate(year2_rank)}
                growth_rankings = {item[0]: index+1 for index, item in enumerate(growth_rank)}

                rankings_data.append({
                    'indicator': indicator.indicator,
                    'year1_value': year1_value,
                    'year2_value': year2_value,
                    'growth': growth,
                    'year1_rank': year1_rankings.get(indicator.indicator, 51),
                    'year2_rank': year2_rankings.get(indicator.indicator, 51),
                    'growth_rank': growth_rankings.get(indicator.indicator, 51),
                })
            else:
                # Handle the case where data for either year is missing
                print(f"Missing data for Indicator: {indicator.indicator} in years {year1} or {year2}")
                rankings_data.append({
                    'indicator': indicator.indicator,
                    'year1_value': None,
                    'year2_value': None,
                    'growth': None,
                    'year1_rank': None,
                    'year2_rank': None,
                    'growth_rank': None,
                })

        # Debugging: Check the final rankings data
        print(f"Rankings Data: {rankings_data}")

        # Sort indicators by group
        sorted_rankings = sorted(rankings_data, key=lambda x: x['indicator'])

        return render(request, 'rankings/rankings.html', {
            'states': states,
            'years': years,
            'selected_state': selected_state,
            'year1': year1,
            'year2': year2,
            'rankings_data': sorted_rankings
        })
