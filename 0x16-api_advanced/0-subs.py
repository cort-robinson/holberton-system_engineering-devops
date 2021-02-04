#!/usr/bin/python3
"""defines number_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of
    subscribers for a given subreddit. If
    subreddit is invalid, returns 0
    """
    try:
        return requests.get("https://www.reddit.com/r/{}/about.json".format(
                            subreddit),
                            headers={'user-agent': "Cort's requests"},
                            allow_redirects=False).json()['data'].get(
                            'subscribers')
    except Exception:
        return 0
