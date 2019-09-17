"""
简易爬虫模块
"""
from urllib import request
import gzip
import re


class Spider():
    """
    这是一个爬虫类
    """
    # url = "https://www.huya.com/g/5485" 更改其他地址，一样可以获取数据
    url = "https://www.huya.com/g/lol"
    url1 = "https://www.douyu.com/g_LOL"

    root_pattern = '<li class="game-live-item" gid="\d*">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    num_pattern = '<i class="js-num">([\s\S]*)</i>'

    def __fetch_content(self):
        """
        获取页面内容
        :return:
        """
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
        # print(str(content, encoding='utf-8'))
        return str(content, encoding='utf-8')

    def __analysis(self, html):
        root_html_list = re.findall(Spider.root_pattern, html)

        # 不同意义代码块之间可以添加空行
        anchors = []
        for root_html in root_html_list:
            name_list = re.findall(Spider.name_pattern, root_html)
            num_list = re.findall(Spider.num_pattern, root_html)
            anchor = {"name": name_list, "number": num_list}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        """
        精炼数据
        :param anchors:
        :return:
        """
        l = lambda anchor: {
            "name": anchor["name"][0].strip(),
            "number": anchor["number"][0]
        }
        return map(l, anchors)

    def __sort(self, anchors):
        """
        排序处理
        :param anchors:
        :return:
        """
        anchors = sorted(anchors, key=self.__sort_key, reverse=True)
        return anchors

    def __sort_key(self, anchor):
        """
        排序key
        :param anchor:
        :return:
        """
        # \d* [\d.]+
        r = re.findall("[\d.]+", anchor["number"])
        number = float(r[0])
        if "万" in anchor["number"]:
            number *= 10000
        return number

    def __show(self, anchors):
        """
        展示数据
        :param anchors:
        :return:
        """
        # for anchor in anchors:
        #     print(anchor["name"], anchor["number"])
        for i in range(0, len(anchors)):
            print(str(i+1) + ":\t" + anchors[i]["name"] + "\t" + anchors[i]["number"])

    def go(self):
        html = self.__fetch_content()
        anchors = self.__analysis(html)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()
