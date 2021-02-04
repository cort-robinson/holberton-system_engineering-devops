#!/usr/bin/python3
"""defines recurse"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Queries Reddit API and returns list with titles
    of all hot articles for given subreddit
    """
    request = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(
            subreddit),
        headers={'user-agent': "Cort's requests"},
        params={'after': after},
        allow_redirects=False)
    if request.status_code != 200:
        return None
    request = request.json()
    after = request.get('data').get('after')
    for post in request.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
