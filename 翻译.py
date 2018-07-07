import requests
import json

import sys


class Fanyi(object):
    def __init__(self, word):
        self.detect_url = "http://fanyi.baidu.com/langdetect"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.word = word

    def get_date(self,url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return response.content.decode()

    def run(self):
        data = {"query": self.word}
        res = self.get_date(self.detect_url, data)
        res = json.loads(res)
        # print(res)
        data["from"] = res["lan"]
        data["to"] = "en" if res["lan"] == "zh" else "zh"
        res = self.get_date(self.trans_url, data)
        res = json.loads(res)
        print(res["trans"][0]["dst"])
if __name__ == '__main__':
    word = sys.argv[1]
    fanyi = Fanyi(word)
    fanyi.run()
