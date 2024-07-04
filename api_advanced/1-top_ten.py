#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests



def top_ten(subreddit):
    """Return prints the titles of the first 10 hot posts listed for a given subreddit.
    if not return 0."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        if not posts:
            print(None)
            return
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception as e:
        print(None)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])