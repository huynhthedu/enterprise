import pandas as pd
from django.core.management.base import BaseCommand
from rankings.models import Indicator

class Command(BaseCommand):
    help = "Import data from Excel"

    def handle(self, *args, **kwargs):
        file_path = 'https://docs.google.com/spreadsheets/d/1XtyjoLNN_OpasZIVqW9yfj7CjXREQRR7/export?format=xlsx'  # Update with your file path
        try:
            excel_file = pd.ExcelFile(file_path, engine='openpyxl')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading Excel file: {e}"))
            return

        sheets = excel_file.sheet_names
        for sheet in sheets:
            self.stdout.write(f"Processing sheet: {sheet}")
            df = pd.read_excel(file_path, sheet_name=sheet, engine='openpyxl')
            df.columns = df.columns.str.strip()  # Clean column names

            for _, row in df.iterrows():
                for year in range(1998, 2024):
                    if str(year) in df.columns and not pd.isna(row.get(str(year))):
                        Indicator.objects.create(
                            state=row['State'],
                            group=row['Group'],
                            indicator=row['Indicator'],
                            unit=row['Unit'],
                            source=row['Source'],
                            year=year,
                            value=row[str(year)]
                        )
                    else:
                        print(f"Skipping missing year {year} for row: {row}")

        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
