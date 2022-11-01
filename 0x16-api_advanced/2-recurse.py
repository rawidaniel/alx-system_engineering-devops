#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        return all hot articles for a given subreddit
        return None if invalid subreddit given
    """
    headers = {
      'User-Agent': 'My User Agent 1.0'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers=headers,
                     allow_redirects=False, params={'after': after})
    # append top titles to hot_list
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return None
    for e in results:
        hot_list.append(e.get('data').get('title'))
    # get next param "after" else nothing else to recurse
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
