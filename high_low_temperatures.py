from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.figure import Figure
import sys

# path = Path('weather_data/sitka_weather_2021_simple.csv')
# path = Path('weather_data/bialystok_weather_2024.csv')
path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
date_index, tmin_index, tmax_index, name_index = None, None, None, None

for index, header in enumerate(header_row):
    print(index, header)
    h_up = header.upper()
    if h_up == 'DATE':
        date_index = index
    elif h_up == 'TMIN':
        tmin_index = index
    elif h_up == 'TMAX':
        tmax_index = index
    elif h_up == 'NAME':
        name_index = index


dates = []
highs = []
lows = []

name, date = '', None

for row in reader:
    name = row[name_index]
    date = datetime.strptime(row[date_index], '%Y-%m-%d')
    
    if date < datetime(2025, 1, 1):
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            pass
            # print(f"Missing value for date {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    else:
        break


fgr, ax = plt.subplots()
plt.style.use('seaborn-v0_8-deep')

ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

name = name.split(',')[0].strip().title()
title = f'Daily High And Low Temperatures, {name}, {date.year}'
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature F', fontsize=16)
ax.tick_params(labelsize=8)

fgr.autofmt_xdate()
fgr.set_size_inches(12, 6)

plt.show()
