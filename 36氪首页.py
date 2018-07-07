import json
import re
import requests

class Kr(object):
    def __init__(self):
        self.url = "http://36kr.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    def get_data_from_url(self, url):
        response = requests.get(url)
        return response.content.decode()
    def get_json(self, data):
        data_str = re.findall(r'<script>var props=(.+?),locationnal={".+</script>', data)[0]
        obj = json.loads(data_str)
        return obj
    def save_data(self, obj):
        with open("36kr.json","w", encoding="utf8")as f:
            json.dump(obj,f,ensure_ascii=False)
    def run(self):
        data = self.get_data_from_url(self.url)
        # print(data)
        obj = self.get_json(data)
        self.save_data(obj)

if __name__ == '__main__':
    kr = Kr()
    kr.run()
