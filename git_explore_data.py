import json
from pathlib import Path

path = Path('git_data/git_python_projects.json')
contents = path.read_text()

json_data = json.loads(contents)

items = json_data['items']

print(len(items))