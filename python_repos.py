import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

resp_dict = r.json()
print(resp_dict.keys())