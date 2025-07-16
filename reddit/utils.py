def extract_username_from_url(url):
    import re
    match = re.search(r"reddit.com/user/([^/]+)/?", url)
    return match.group(1) if match else None


def format_user_data(posts, comments):
    result = ""
    for p in posts[:5]:
        result += f"[POST] Title: {p.get('title')}\nText: {p.get('selftext', '')}\n---\n"
    for c in comments[:10]:
        result += f"[COMMENT] {c.get('body')}\n---\n"
    return result