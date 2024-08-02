from pathlib import Path
import csv
import plotly.express as px

path = Path('fire_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

lat_ind, lon_ind, br_ind = None, None, None

for index, header in enumerate(header_row):
    h_lo = header.lower()
    if h_lo == 'latitude':
        lat_ind = index
    elif h_lo == 'longitude':
        lon_ind = index
    elif h_lo == 'brightness':
        br_ind = index
    print(header)

lats, lons, brs = [], [], []

for row in reader:
    try:
        lat = float(row[lat_ind])
        lon = float(row[lon_ind])
        br = float(row[br_ind])
    except ValueError as err:
        print(f"Can't parse value to float.")
    else:
        lats.append(lat)
        lons.append(lon)
        brs.append(br)

fig = px.scatter_geo(lat=lats, lon=lons, title='World Fires',
                     color=brs,
                     size=brs,
                     color_continuous_scale='RedOr',
                     labels={'color': 'brightness'},
                     projection='natural earth'
                     )

fig.show()


