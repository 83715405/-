import json
import re
import requests


class Guokrspider(object):
    def __init__(self):
        self.url = "https://www.guokr.com/ask/highlight/?page=1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }
        self.pre = "https://www.guokr.com"

    def get_data_from_url(self, url):
        response = requests.get(url)
        return response.content.decode()

    def get_data_list(self, data):
        '''<h2><a target="_blank" href="https://www.guokr.com/question/668948/">
        子弹能射穿多少本书，与那一摞书本的本数多少有何关系？</a></h2>'''
        data_list = re.findall(r'<h2><a target="_blank" href="(.+?)">(.+?)</a></h2>', data, re.S)
        '<a href="/ask/highlight/?page=2">下一页</a>'
        next_url = re.findall('<a href="(.+?)">下一页</a>', data)
        next_url = self.pre + next_url[0] if len(next_url) != 0 else None
        print(next_url)
        return data_list, next_url

    def save_data(self, data_list):
        with open("guokr1.text", "a", encoding="utf8")as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        url = self.url
        while url is not None:
            data = self.get_data_from_url(url)
            # print(data)
            data_list, url = self.get_data_list(data)
            self.save_data(data_list)


if __name__ == '__main__':
    gkr = Guokrspider()
    gkr.run()
