import requests
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.134 Safari/537.36"
    # "accept": "*/*"
}


def get_data(headers):
    url = 'https://twitter.com/ExoScripts/status/1403108584381194240'
    r = requests.get(url=url, headers=headers)
    with open('index.html', 'w') as file:
        file.write(r.text)


def main():
    get_data(headers=headers)


if __name__ == '__main__':
    main()
