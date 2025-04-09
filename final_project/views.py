from django.shortcuts import render
from data.models import C2023B, Hd2023, Ic2023Ay, RankingsIndicator, Effy2023, Adm2023, State, Sector
from .models import LibraryDimension
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
from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma
import zipfile
import io
import requests
import numpy as np




# DIRECT DATA
HD_URL = "https://nces.ed.gov/ipeds/datacenter/data/HD2023.zip"
LIBRARY_URL = "https://nces.ed.gov/ipeds/datacenter/data/AL{}.zip"

# Function to download and extract CSV from ZIP URL
def download_and_extract_csv(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            # List contents of the ZIP file
            print("Contents of the ZIP file:", z.namelist())
            
            # Check if the file exists in the archive
            if file_name in z.namelist():
                with z.open(file_name) as f:
                    return pd.read_csv(f, encoding="latin1", dtype=str)
            else:
                raise KeyError(f"There is no item named '{file_name}' in the archive")
    return None

# Fetch institution names
def get_institution_names():
    hd_data = download_and_extract_csv(HD_URL, "hd2023.csv")
    return hd_data[['UNITID', 'INSTNM', 'STABBR', 'SECTOR']].dropna()

# Fetch admissions data for all years
def get_library_data():
    columns_to_melt = ['LPBOOKS', 'LEBOOKS', 'LEDATAB', 'LPMEDIA', 'LEMEDIA', 'LPSERIA', 'LESERIA', 'LEXOMTL']
    all_data = []
    for year in range (2019, 2024):
        file_name = f"al{year}.csv"
        url = LIBRARY_URL.format(year)
        df = download_and_extract_csv(url, file_name)
        if df is not None:
            df["Year"] = year

            # Only keep columns that exist in the dataset
            available_columns = ["UNITID", "LCOLELYN"] + [col for col in columns_to_melt if col in df.columns]
            df = df[available_columns + ["Year"]]

            # Print columns to verify
            print(f"Columns in DataFrame for year {year}: {df.columns}")

            # Unpivot data (Convert Wide to Long Format)
            df_melted = df.melt(id_vars=["UNITID", "LCOLELYN", "Year"], 
                                var_name="Item", 
                                value_name="Value")

            # Append to list
            all_data.append(df_melted)

            print(f"Loaded {year}: {len(df_melted)} rows")  # Debugging
    df = pd.concat(all_data, ignore_index=True)
            
    return df.dropna(subset=['Value'])


# Process and merge data
def get_processed_data():
    institutions = get_institution_names()
    library = get_library_data()
    
    # Convert LibraryDimension QuerySet to DataFrame
    library_dimension_queryset = LibraryDimension.objects.all()
    library_dimension_df = pd.DataFrame(list(library_dimension_queryset.values()))
    # Merge with institution names
    library = library.merge(institutions, on="UNITID", how="left")
    library = library.merge(library_dimension_df, left_on="Item", right_on="lb_id", how="left")
    
    # Print missing values for debugging
    print("Missing values after merge:\n", library.isnull().sum())

    # Remove only rows where UNITID or YEAR is missing, keep others
    library = library.dropna(subset=["UNITID", "Item", "INSTNM", "Year", "LCOLELYN"])
    
    # Debugging: Check if years are still missing
    print("Years available in cleaned data:", sorted(library["Year"].unique()))

    return library



# View for the dashboard
def library(request):
    institutions = get_institution_names()
    institutions_list = institutions.to_dict(orient="records")

    # Set default institution as "University of Mississippi" if none is selected
    default_instnm = "University of Mississippi"
    selected_instnm = request.GET.get("institution", default_instnm)

    # Load processed data
    library = get_processed_data()

    # Find the selected institution's details
    selected_inst = institutions[institutions["INSTNM"] == selected_instnm]
    if selected_inst.empty:
        return JsonResponse({"error": "Institution not found"}, status=404)

    unitid = selected_inst["UNITID"].values[0]
    sector = selected_inst["SECTOR"].values[0]
    state = selected_inst["STABBR"].values[0]

    print(library.head())

    return render(request, "final_project/final.html", {
        "institutions": institutions_list,
        "selected_institution": selected_instnm,
    })


