import json
import re
import requests


class Guokrspider(object):
    def __init__(self):
        self.url = "https://www.guokr.com/ask/highlight/?page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }
        self.urllist = [self.url.format(i) for i in range(1, 100)]

    def get_data_from_url(self, url):
        response = requests.get(url)
        return response.content.decode()

    def get_data_list(self, data):
        '''<h2><a target="_blank" href="https://www.guokr.com/question/668948/">
        子弹能射穿多少本书，与那一摞书本的本数多少有何关系？</a></h2>'''
        data_list = re.findall(r'<h2><a target="_blank" href="(.+?)">(.+?)</a></h2>', data, re.S)
        return data_list

    def save_data(self, data_list):
        with open("guokr.text", "a", encoding="utf8")as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        for url in self.urllist:
            data = self.get_data_from_url(url)
            data_list = self.get_data_list(data)
            self.save_data(data_list)


if __name__ == '__main__':
    gkr = Guokrspider()
    gkr.run()
