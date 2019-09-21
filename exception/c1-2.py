# 或 from requests import ConnectionError, ReadTimeout
# from requests.exceptions import ConnectionError, ReadTimeout

import requests
from requests import ReadTimeout, ConnectTimeout


def get_page(url):
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            return response.text
        else:
            print("Get page Failed", response.status_code)
            return None
    except(ConnectionError, ReadTimeout, ConnectTimeout):
        print("Calling failed", url)
        return None


def main():
    url = "https://www.baidu.com/"
    # ConnectTimeout
    # url = "https://www.google.com/"
    print(get_page(url))


# 入口方法
if __name__ == '__main__':
    main()
