import requests
import json
from requests_oauthlib import OAuth1
import secrets as s

AUTH = OAuth1(s.API_KEY, s.API_SECRET, s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)


def run():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    r = requests.get(url, auth=AUTH)
    print(r.status_code)


def list_by_username(username):
    url = 'https://api.twitter.com/1.1/friends/list.json?screen_name={username}'\
        .format(username=username)
    r = requests.get(url, auth=AUTH)
    print(r.status_code)


def list_by_id(user_id):
    url = 'https://api.twitter.com/1.1/friends/ids.json?user_id={user_id}'\
        .format(user_id=user_id)
    r = requests.get(url, auth=AUTH)
    print(r.status_code)


def get_username_from_id(user_id):
    url = 'https://api.twitter.com/1.1/users/lookup.json?user_id={user_id}'\
        .format(user_id=user_id)
    r = requests.get(url, auth=AUTH)
    print(r.status_code)

if __name__ == "__main__":
    get_username_from_id('20257992')
