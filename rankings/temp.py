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

    # Order the DataFrame by group
    df = df.sort_values(by='group')

    # Draw separate horizontal bar charts for value2 of all indicators and sort them in descending order
    plot_urls = []
    for indicator in selected_indicators:
        fig, ax = plt.subplots(figsize=(16, 24))  # Increase figure size
        indicator_df = df[df['indicator'] == indicator].sort_values(by='value2', ascending=True)
        
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

    return render(request, 'rankings/select_state.html', context)
