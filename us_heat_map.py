from urllib.request import urlretrieve
import json
import pandas as pd
import plotly.express as px

# Download GeoJSON file
geojson_url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
geojson_path = 'geojson-counties-fips.json'
urlretrieve(geojson_url, geojson_path)

# Download CSV file
csv_url = 'https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv'
csv_path = 'fips-unemp-16.csv'
urlretrieve(csv_url, csv_path)

# Load GeoJSON data
with open(geojson_path) as response:
    counties = json.load(response)

# Load CSV data into Pandas DataFrame
df = pd.read_csv(csv_path, dtype={"fips": str})

# Create a choropleth map using Plotly Express
fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                    color_continuous_scale="Viridis",
                    range_color=(0, 12),
                    scope="usa",
                    labels={'unemp': 'Unemployment Rate'})

# Update layout
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Show the map
fig.show()
