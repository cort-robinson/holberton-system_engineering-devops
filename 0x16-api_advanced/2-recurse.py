#!/usr/bin/python3
"""defines recurse"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Queries Reddit API and returns list with titles
    of all hot articles for given subreddit
    """
    request = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(
            subreddit),
        headers={'user-agent': "Cort's requests"},
        allow_redirects=False).json().get('data').get('children')
    for post in request:
        hot_list.append(post.get('data').get('title'))
    return hot_list
