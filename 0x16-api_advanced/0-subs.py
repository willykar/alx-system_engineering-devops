#!/usr/bin/python3
"""A module to query subscribers on redit api"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users,
    total subscribers) for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
