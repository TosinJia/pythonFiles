
from urllib import request
import gzip


class Spider():
    url = "https://www.huya.com/g/lol"
    url1 = "https://www.douyu.com/g_LOL"

    def __fetch_content(self):
        # 方式一
        r = request.urlopen(Spider.url)
        content = r.read()
        print(content.decode('utf-8'))
        # 方式二 两种方式获取数据不一致
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        req = request.Request(url=Spider.url, headers=headers)
        content = request.urlopen(req).read()
        # encoded_content = gzip.decompress(content).decode("utf-8")
        print(content.decode('utf-8'))

    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()
