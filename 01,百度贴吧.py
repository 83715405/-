import requests


class Tb_spider(object):
    """
    1,准备url列表
    2,发起请求,获取相应内容
    3,解析新的url加入url列表
    4,入库
    """

    def __init__(self, name, start, end):
        self.url_list = []
        self.name = name
        self.start = start
        self.end = end
        self.url_modal = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }

    def get_url(self):
        return [self.url_modal.format(self.name, (i - 1) * 50) for i in range(self.start, self.end + 1)]

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_page(self, page, page_num):
        file_name = self.name + '_第' + str(page_num) + "页"+".html"
        with open(file_name, "w") as f:
            f.write(page)

    def run(self):
        url_li = self.get_url()
        for url in url_li:
            page = self.get_page(url)
            page_num = url_li.index(url)+1
            self.save_page(page, page_num)

if __name__ == '__main__':
    tb = Tb_spider("风景图", 1, 4)
    tb.run()
