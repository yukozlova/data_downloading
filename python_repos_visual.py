import plotly.express as px
import requests

def show_repos(language):
    url = "https://api.github.com/search/repositories"
    url += f"?q=language:{language}+sort:stars+stars:>20000"

    headers = {'Accept': 'application/vnd.github.v3+json'}

    r = requests.get(url=url, headers=headers)
    print(f"Status code: {r.status_code}")

    resp_dict = r.json()
    items = resp_dict['items']

    repo_names, stars = [], []
    hover_texts = []
    repo_links = []

    for item in items:
        repo_name = item['name']
        repo_url = item['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(int(item['stargazers_count']))
        owner = item['owner']['login']
        descr = item['description']
        hover_text = f"{owner}<br />{descr}"
        hover_texts.append(hover_text)

    try:
        title = f"Most-starred {language} projects on github".title()
        labels = {'x': 'Repository', 'y': 'Stars'}
        fgr = px.bar(x=repo_links, y=stars, title=title, labels=labels,
                    hover_name=hover_texts)

        fgr.update_layout(title_font_size=28, xaxis_title_font_size=20,
                        yaxis_title_font_size=20)

        fgr.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

        fgr.show()
    except Exception:
        print(f"Error len = ({len(repo_links)}, {len(stars)})")