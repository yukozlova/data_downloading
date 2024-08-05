import requests
from operator import itemgetter
import plotly.express as px

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

resp = requests.get(url)
print(f"Status code: {resp.status_code}")

submission_ids = resp.json()

print(len(submission_ids))

subm_dicts = []

for id in submission_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    resp = requests.get(url)
    print(f"Status code for id={id}: {resp.status_code}")
    resp_dict = resp.json()
    
    try:
        subm_dict = {
            'title': resp_dict['title'],
            'link': resp_dict['url'],
            'comments': resp_dict['descendants']
        }
    except Exception:
        print(f"Failed for id={id}.")
    else:
        subm_dicts.append(subm_dict)

for subm in sorted(subm_dicts[:1], key=itemgetter('comments'), reverse=True):
    print(f"\nTitle: {subm['title']}")
    print(f"\Discussion link: {subm['link']}")
    print(f"\Comments: {subm['comments']}")

title = f"Most actively discussed articles on Hacker News".title()
labels = {'x': 'Article', 'y': 'Comments'}

fgr = px.bar(x=[f"<a href='{s['link']}'>{s['title']}</a>" for s in subm_dicts], 
             y=[s['comments'] for s in subm_dicts],
             title=title,
             labels=labels,
             )

fgr.update_traces(marker_color='SteelBlue', marker_opacity =0.6)

fgr.show()




