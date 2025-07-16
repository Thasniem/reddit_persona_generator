import requests
import json
from pathlib import Path

def fetch_reddit_data(username, save_path='data/raw_posts_comments.json'):
    base_url = "https://api.pushshift.io/reddit"
    posts_url = f"{base_url}/submission/search?author={username}&size=50"
    comments_url = f"{base_url}/comment/search?author={username}&size=100"

    posts = requests.get(posts_url).json().get("data", [])
    comments = requests.get(comments_url).json().get("data", [])

    data = {"posts": posts, "comments": comments}
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data