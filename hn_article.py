import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/41162311.json"

resp = requests.get(url=url)
resp_dict = resp.json()

readable_content = json.dumps(resp_dict, indent=4)
print(readable_content)
