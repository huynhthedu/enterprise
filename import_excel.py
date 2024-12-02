import pandas as pd
from rankings.models import Indicator  # Change to your actual model

# Path to the downloaded file
file_path = r'D:\Download\State_data.xlsx'

# Read the Excel file (all sheets)
excel_data = pd.ExcelFile(file_path)

# Loop through all sheets in the Excel file
for sheet_name in excel_data.sheet_names:
    # Read each sheet into a DataFrame
    df = excel_data.parse(sheet_name)

    # Ensure the required columns are in the dataframe
    required_columns = ['ID', 'Group', 'Indicator', 'Unit', 'Source'] + [str(year) for year in range(1997, 2024)]
    if not all(col in df.columns for col in required_columns):
        print(f"Sheet '{sheet_name}' does not contain all required columns.")
        continue

    # Loop through each row and save it to the model
    for _, row in df.iterrows():
        # Extract the common values
        group = row['Group']
        indicator = row['Indicator']
        unit = row['Unit']
        source = row['Source']

        # Loop through the years (1998-2024)
        for year in range(1997, 2024):
            # Get the value for this year
            value = row.get(str(year), None)

            if pd.notna(value):  # Only insert if the value is not NaN (missing)
                # Create or update the record in the Indicator model
                Indicator.objects.create(
                    id=row['ID'],  # Assuming ID from the Excel is unique
                    group=group,
                    indicator=indicator,
                    unit=unit,
                    source=source,
                    year=year,
                    value=value
                )

    print(f"Finished importing data from sheet '{sheet_name}'.")

print("Data import complete.")
