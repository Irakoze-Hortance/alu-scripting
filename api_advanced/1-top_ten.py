#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    try:
        response = requests.get(subreddit_url, headers=headers,allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(None)
        return
    
    if response.status_code == 200:
        try:
            json_data = response.json()
            posts = json_data.get('data').get('children', [])
            if not posts:
                print(None)
                return
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        except (ValueError, KeyError):
            print(None)
    else:
        print(None)
