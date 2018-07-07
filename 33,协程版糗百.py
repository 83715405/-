from gevent import monkey
monkey.patch_all()
import json
from multiprocessing import Process
from multiprocessing import JoinableQueue
import gevent
import requests
from gevent.pool import Pool
# from multiprocessing.dummy import Pool
from queue import Queue

import time
from lxml import etree


class QiuShi(object):
    def __init__(self):
        self.url_madel = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        }
        self.url_queue = Queue()
        self.response_queue = Queue()
        self.data_queue = Queue()
        self.pool = Pool(6)

    def add_url_to_queue(self):
        # url_list = [self.url_madel.format(i) for i in range(1, 14)]
        # return url_list
        for i in range(1, 14):
            self.url_queue.put(self.url_madel.format(i))

    def add_page_to_queue(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            print(response.status_code)
            if response.status_code != 200:
                # url_queue的unfinished_tasks 增加1
                self.url_queue.put(url)
            else:
                # 把响应内容添加到响应列表
                self.response_queue.put(response.content)
                # 到这儿,当前这个url的任务已经处理完成了
                # 饶昂url_queue的unfinished_tasks减少1
            self.url_queue.task_done()

    def add_data_to_queue(self):
        while True:
            page = self.response_queue.get()
            element = etree.HTML(page)
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
            self.data_queue.put(data_list)
            self.response_queue.task_done()

    def save_data(self):
        while True:
            data_list = self.data_queue.get()
            with open("协程.text", "a", encoding="utf8")as f:
                for data in data_list:
                    json.dump(data, f, ensure_ascii=False)
                    f.write("\n")
            self.data_queue.task_done()

    def excute_more_tasks(self, target, count):
        for i in range(0, count):
            self.pool.apply_async(target)

    def run(self):

        self.excute_more_tasks(self.add_url_to_queue, 1)
        self.excute_more_tasks(self.add_page_to_queue, 2)
        self.excute_more_tasks(self.add_data_to_queue, 3)
        self.excute_more_tasks(self.save_data, 1)
        time.sleep(1)
        self.url_queue.join()
        self.response_queue.join()
        self.data_queue.join()
        # self.url_queue.join()
        # self.response_queue.join()
        # self.data_queue.join()
        # for url in url_list:
        #     data = self.get_data_from_url(url)
        #     data_list = self.get_dz_list_from_data(data)
        #
        # self.save_data(data_list)

    def get_first_from_list(self, ls):
        return ls[0] if len(ls) != 0 else None


if __name__ == '__main__':
    qss = QiuShi()
    qss.run()
