#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    A method that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the
    given subreddit
    Return None If not a valid subreddit
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if res.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
