import pandas as pd
import numpy as np
import geopandas as gpd
import folium

# population date from Statistics Canada
df = pd.read_csv("9810000701_databaseLoadingData.csv", encoding="ISO-8859-1")
census_21 = df[["DGUID", "VALUE"]]

# census boundry file from Statistics Canada
canada_geo = gpd.read_file("lcd_000a21a_e.shp")

# set the scale
threshold_scale = np.linspace(census_21["VALUE"].min(),
                              census_21["VALUE"].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist()
threshold_scale[-1] = threshold_scale[-1] + 1 

# choropleth map
canada_map = folium.Map(location=[53.576459, -96.090255], 
                        zoom_start=4)
canada_map.choropleth(
    geo_data=canada_geo,
    data=census_21,
    columns=["DGUID", "VALUE"],
    key_on="feature.properties.DGUID",
    threshold_scale=threshold_scale,
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in Canada (Census 2021)")

canada_map
