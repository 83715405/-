import re
import requests


class NeiHan(object):
    def __init__(self):
        self.url = 'http://www.neihanpa.com/article/list_5_1.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }
        self.pre = "http://www.neihanpa.com/article/"
    def get_data_from_url(self, url):
        response = requests.get(url)
        return response.content.decode("gbk")

    def get_duzi_list_from_data(self, data):
        '''<div class="f18 mb20"><p>(.+?)</p></div>'''
        # for dz in data:
        data_list = re.findall(r'<div class="f18 mb20">(.+?)</div>', data, re.S)
        "<li><a href='list_5_2.html'>下一页</a></li>"
        next_url = re.findall(r"<li><a href='(.+?)'>下一页</a></li>", data)[0]
        next_url = self.pre + next_url
        print(next_url, type(next_url))
        for dz in data_list:
            index = data_list.index(dz)
            dz = re.sub('<.*>|\s', "", dz)
            dz = re.sub(r"&ldquo;|&rdquo;", '"', dz)
            dz = re.sub(r'&hellip;', '...', dz)
            data_list[index] = dz
        return data_list, next_url

    def save_dz(self, dz_list):
        with open("dz.txt", "a", encoding="utf-8")as f:
            for dz in dz_list:
                f.write(dz)
                f.write("\n")

    def run(self):
        url = self.url
        while url is not None:
            data = self.get_data_from_url(url)
            # print(data)
            dz_list, url = self.get_duzi_list_from_data(data)
            self.save_dz(dz_list)


if __name__ == '__main__':
    duanzi = NeiHan()
    duanzi.run()
