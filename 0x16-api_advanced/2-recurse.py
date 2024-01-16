#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests

PAGE = None


def recurse(subreddit, hot_list=[]):
    global PAGE
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'after': PAGE}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])

    PAGE = data['data']['after']
    if PAGE is not None:
        return recurse(subreddit, hot_list)
    else:
        return hot_list
