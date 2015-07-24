import requests


def run():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print(r.status_code)


if __name__ == "__main__":
    run()
