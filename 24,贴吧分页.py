from lxml import etree
import requests
import json


class TieBa(object):
    def __init__(self, tb_name):
        self.url_lodal = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}"
        self.name = tb_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}
        self.url = self.url_lodal.format(tb_name)
        print(self.url)
        self.pre_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"

    def get_data_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_page_from_data(self, data):
        element = etree.HTML(data)
        print(element)
        a_s = element.xpath("//div[contains(@class,'i')]/a")
        net = element.xpath("/html/body/div/form[1]/div/a[text()='下一页']/@href")
        next_url = self.pre_url + net[0] if len(net) != 0 else None
        print(next_url)
        data_list = []
        for a in a_s:
            item = {}
            item["title"] = a.xpath('./text()')[0]
            item["detail_url"] = self.pre_url + a.xpath('./@href')[0]
            item["img_urls"] = self.get_url_from_img(item['detail_url'])
            data_list.append(item)
        return data_list, next_url
    def get_url_from_img(self, detail_url):
        img_list = []
        while detail_url is not None:
            page = self.get_data_from_url(detail_url)
            element = etree.HTML(page)
            images = element.xpath('//img[@class="BDE_Image"]/@src')
            for img in images:
                img = requests.utils.unquote(img)
                img = img.split('src=')[1]
                print(img)
                img_list.append(img)
            next_url = element.xpath("//a[text()='下一页']/@href")
            detail_url = self.pre_url+next_url[0] if len(next_url) != 0 else None
    def save_data(self, data_list):
        file_name = self.name + ".txt"
        with open(file_name, "a", encoding="utf8")as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        url = self.url
        while url is not None:
            data = self.get_data_from_url(url)
            # print(data)
            data_list, url = self.get_page_from_data(data)
            # print(data_list)
            self.save_data(data_list)


if __name__ == '__main__':
    tieba = TieBa("做头发")
    tieba.run()
