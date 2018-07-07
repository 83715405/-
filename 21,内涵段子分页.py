import re
import requests


class NeiHan(object):
    def __init__(self):
        self.url = 'http://www.neihanpa.com/article/list_5_{}.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }

    def get_data_from_url(self, url):
        response = requests.get(url)
        return response.content.decode("gbk")

    def get_duzi_list_from_data(self, data):
        '''<div class="f18 mb20"><p>(.+?)</p></div>'''
        # for dz in data:
        data_list = re.findall(r'<div class="f18 mb20">(.+?)</div>', data, re.S)
        for dz in data_list:
            index = data_list.index(dz)
            dz = re.sub('<.*>|\s', "", dz)
            dz = re.sub(r"&ldquo;|&rdquo;", '"', dz)
            dz = re.sub(r'&hellip;', '...', dz)
            data_list[index] = dz
        return data_list

    def save_dz(self, dz_list):
        with open("dz.txt", "a", encoding="utf-8")as f:
            for dz in dz_list:
                f.write(dz)
                f.write("\n")

    def run(self):
        url_list = [self.url.format(i) for i in range(1, 507)]
        for url in url_list:
            data = self.get_data_from_url(url)
            # print(data)
            dz_list = self.get_duzi_list_from_data(data)
            self.save_dz(dz_list)


if __name__ == '__main__':
    duanzi = NeiHan()
    duanzi.run()
