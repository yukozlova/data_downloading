from pathlib import Path
import json

path = Path('git_data/git_python_projects.json')
contents = path.read_text()

json_data = json.loads(contents)
path = Path('git_data/readable_git_data.json')
readable_contents = json.dumps(json_data, indent=4)
path.write_text(readable_contents)
