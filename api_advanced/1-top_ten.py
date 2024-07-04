#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        print(None)
        return

    if response.status_code == 200:
        try:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return

            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        except (ValueError, KeyError):
            print(None)
    else:
        print(None)
