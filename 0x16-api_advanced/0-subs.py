#!/usr/bin/python3
"""
queries the Reddit API and returns the total number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Reterive total number of subscribers for given subreddit
    Reterive o if invalid subreddit given
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
      'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get("subscribers")
    if not subscribers:
        return 0
    return subscribers
