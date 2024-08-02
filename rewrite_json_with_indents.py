from pathlib import Path
import json

path = Path('eq_data/eq_data_2024_08_01.geojson')
contents = path.read_text()

json_data = json.loads(contents)
path = Path('eq_data/readable_ed_data_1_day.geojson')
readable_contents = json.dumps(json_data, indent=4)
path.write_text(readable_contents)
