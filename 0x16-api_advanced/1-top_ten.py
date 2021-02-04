#!/usr/bin/python3
"""defines top_ten"""
import json
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of
    first 10 hot posts for given subreddit
    """
    try:
        request = requests.get(
            'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
                subreddit),
            headers={'user-agent': "Cort's requests"},
            allow_redirects=False).json().get('data').get('children')
        for post in request:
            print(post.get('data').get('title'))
    except Exception:
        print(None)
