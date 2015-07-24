import requests
from requests_oauthlib import OAuth1
import secrets as s


def run():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1(s.API_KEY, s.API_SECRET, s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
    r = requests.get(url, auth=auth)
    print(r.status_code)


def list_by_username(username):
    url = 'https://api.twitter.com/1.1/friends/list.json?screen_name={username}'\
        .format(username=username)
    auth = OAuth1(s.API_KEY, s.API_SECRET, s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
    r = requests.get(url, auth=auth)
    print(r.status_code)


def list_by_id(id):
    url = 'https://api.twitter.com/1.1/friends/ids.json?id={id}'\
        .format(id=id)
    auth = OAuth1(s.API_KEY, s.API_SECRET, s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
    r = requests.get(url, auth=auth)
    print(r.status_code)

if __name__ == "__main__":
    list_by_username('JustinMoen')
