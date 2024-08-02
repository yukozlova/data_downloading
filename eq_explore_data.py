from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_2024_08_01.geojson')    
contents = path.read_text()

all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags = []
lons =[]
lats = []
titles = []

for eq_data in all_eq_dicts:
    mag = eq_data['properties']['mag']
    mag = mag if mag >= 0 else 0
    mags.append(mag)
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    titles.append(eq_data['properties']['title'])

mag_neg = [mag for mag in mags if mag < 0]

print(mag_neg)

# exit()

# mags = [ eq_data['properties']['mag'] for eq_data in all_eq_dicts ]

title = all_eq_data['metadata']['title'].title()
fig = px.scatter_geo(lat=lats, lon=lons, 
                     size=mags,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     title=title,
                     hover_name=titles,
                     )

fig.show()
