
from urllib import request
import gzip
import re


class Spider():
    url = "https://www.huya.com/g/lol"
    url1 = "https://www.douyu.com/g_LOL"

    root_pattern = '<li class="game-live-item" gid="\d*">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    num_pattern = '<i class="js-num">([\s\S]*)</i>'


    def __fetch_content(self):
        # 方式一
        r = request.urlopen(Spider.url)
        content = r.read()
        # print(content.decode('utf-8'))
        # 方式二 两种方式获取数据不一致
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        req = request.Request(url=Spider.url, headers=headers)
        content = request.urlopen(req).read()
        # encoded_content = gzip.decompress(content).decode("utf-8")
        # print(content.decode('utf-8'))
        print(str(content, encoding='utf-8'))
        return str(content, encoding='utf-8')

    def __analysis(self, html):
        root_html_list = re.findall(Spider.root_pattern, html)
        print(root_html_list)
        for root_html in root_html_list:
            name_list = re.findall(Spider.name_pattern, root_html)
            num_list = re.findall(Spider.num_pattern, root_html)
            print(name_list[0], num_list[0])

    def go(self):
        html = self.__fetch_content()
        self.__analysis(html)


spider = Spider()
spider.go()
