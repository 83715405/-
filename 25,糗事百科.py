import json

import requests
from lxml import etree


class QiuShi(object):
    def __init__(self):
        self.url_madel = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }

    def get_url_list(self):
        url_list = [self.url_madel.format(i) for i in range(1, 14)]
        return url_list

    def get_data_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_dz_list_from_data(self, data):
        element = etree.HTML(data)
        dz_s = element.xpath('//div[@id="content-left"]/div')
        data_list = []

        for dz in dz_s:
            item = {}
            item["head_url"] = self.get_first_from_list(dz.xpath('./div[1]/a[1]/img/@src'))
            item['nick_name'] = self.get_first_from_list(dz.xpath('./div[1]/a[2]/h2/text()'))
            gender_class = self.get_first_from_list(dz.xpath("./div[1]/div/@class"))
            if gender_class is not None:
                item['gender'] = "man" if gender_class.find('man') != -1 else 'women'
            else:
                item['gender'] = None
            item['dz_content'] = dz.xpath('./a[1]/div/span[1]/text()')[0]
            item['funny_count'] = dz.xpath('./div/span[1]/i/text()')[0]
            item['comment_count'] = dz.xpath('./div/span/a/i/text()')[0]
            # 把段子信息添加列表中
            data_list.append(item)

            print(dz[0], type(dz))
        return data_list

    def save_data(self, data_list):
        with open("qiubai.text", "a", encoding="utf8")as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            data = self.get_data_from_url(url)
            data_list = self.get_dz_list_from_data(data)

            self.save_data(data_list)

    def get_first_from_list(self, ls):
        return ls[0] if len(ls) != 0 else None


if __name__ == '__main__':
    qss = QiuShi()
    qss.run()
