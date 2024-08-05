import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>20000'

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

resp_dict = r.json()

print(f"Total repositories: {resp_dict['total_count']}")
print(f"Complete results: {not resp_dict['incomplete_results']}")
items = resp_dict['items']
print(f"Number of items received: {len(items)}")


print(f"\nSelected info about item repository:")
for item in items:
    print(f"\nName: {item['name']}")
    print(f"Owner: {item['owner']['login']}")
    print(f"Stars: {item['stargazers_count']}")
    print(f"Repository: {item['html_url']}")
    print(f"Created: {item['created_at']}")
    print(f"Updated: {item['updated_at']}")
    print(f"Description: {item['description']}")
