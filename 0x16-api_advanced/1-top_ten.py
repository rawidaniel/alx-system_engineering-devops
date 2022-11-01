#!/usr/bin/python3
"""
Queries the Reddit API for titles of the first 10 hot
posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Reterive top ten titles for a given subreddit
    Reterive None if invalid subreddit given
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
      'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(url, headers=headers).json()
    top_ten = response.get('data', {}).get('children', [])
    if not top_ten:
        print('None')
    for child in top_ten:
        print(child.get('data').get('title'))
