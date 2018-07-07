import requests


class Tb_splide(object):
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.url_modal = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.headers = {
            "headers": "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

    def get_url(self, page):
        url = self.url_modal.format(self.name, (page - 1) * 50)
        return url

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_page(self, page, page_data):
        file_name = "{}_第{}页.html".format(self.name, page)
        with open(file_name, "w") as f:
            f.write(page_data)

    def run(self):
        page_num = [i for i in range(self.start, self.end)]

        for page in page_num:
            url = self.get_url(page)
            page_data = self.get_page(url)
            self.save_page(page, page_data)


if __name__ == '__main__':
    tb = Tb_splide("心理学", 1, 5)
    tb.run()
