#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
      'User-Agent': 'My User Agent 1.0'
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            word_key = word.lower()
            if word.lower() in title:
                times = len([t for t in title if t == word_key])
                if instances.get(word_key) is None:
                    instances[word_key] = times
                else:
                    instances[word_key] += times

    if after is None:
        if len(instances) == 0:
            return
        sort_key = sorted(instances.keys())
        [print("{}: {}".format(k, instances[k])) for k in sort_key]
    else:
        count_words(subreddit, word_list, instances, after, count)
