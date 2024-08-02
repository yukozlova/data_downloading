from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

path = Path('weather_data/bialystok_weather_2024.csv')
path = Path('weather_data/death_valley_2021_full.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_ind, rain_ind, snow_ind, name_ind = None, None, None, None

for index, header in enumerate(header_row):
    # print(index, header)
    h_up = header.upper()
    if h_up == 'DATE':
        date_ind = index
    elif h_up == 'PRCP':
        rain_ind = index
    elif h_up == 'SNOW':
        snow_ind = index
    elif h_up == 'NAME':
        name_ind = index


# sys.exit()

dates, rains, snows = [], [], []
date, name = None, None

for row in reader:
    date = datetime.strptime(row[date_ind], '%Y-%m-%d')
    name = row[name_ind]
    try:
        rain = 0 if row[3] == '' else float(row[rain_ind]) 
        snow = 0 if row[4] == '' else float(row[snow_ind])
    except Exception:
        print(f"Missing data for date {date}.")
    else:
        dates.append(date)
        rains.append(rain)
        snows.append(snow)

fgr, ax = plt.subplots()

plt.style.use('seaborn-v0_8-deep')

ax.plot(dates, rains, color='blue')
# ax.plot(dates, snows, color='green')

name = name.split(',')[0].strip().title()
title = f'Daily Rains And Snow Depth in {name}, {date.year}'

ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Amount', fontsize=16)
ax.tick_params(labelsize=8)

ax.tick_params(axis='x', rotation=80)

fgr.autofmt_xdate()
fgr.tight_layout()
fgr.set_size_inches(13, 6)

plt.show()
