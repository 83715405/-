from selenium import webdriver
import json
import time
from selenium.webdriver.chrome.options import Options


class DouYu(object):
    '''
    获取房间图片,房间url,房间标题,房间所有者,房间热度信息
    1,创建driver对象
    2,请求直接url
    3,提取数据
    4,保存数据
    5,翻页
    6,退出
    '''

    def __init__(self):
        # 1, 创建driver对象
        self.driver = webdriver.Chrome()
        # 2, 请求直接url
        self.driver.get('https://www.douyu.com/directory/all')
    def get_data(self):
        data_li = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li/a')
        item_li = []
        for data in data_li:
            item = {}
            try:
                item['pic'] = data.find_element_by_xpath('./span/img').get_attribute('src')
                item['url'] = data.get_attribute('href')
                item['title'] = data.find_element_by_xpath('./div/div/h3').text
                item['type'] = data.find_element_by_xpath('./div/div/span').text
                item['author'] = data.find_element_by_xpath('./div/p/span[1]').text
                item['hot'] = data.find_element_by_xpath('./div/p/span[2]').text
            except Exception as e:
                print(e)
                print(item)
            item_li.append(item)
        try:
            next_url = self.driver.find_element_by_partial_link_text('下一页')
        except Exception as e:
            print(e)
            next_url = None
            return item_li,next_url
        return item_li, next_url


    def save_data(self, data_li):
        with open('斗鱼.txt', 'a', encoding='utf8')as f:
            for data in data_li:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')
    def run(self):
        while True:
            # 3, 提取数据
            item_li, next_url = self.get_data()
            # 4, 保存数据
            self.save_data(item_li)
            # 5, 翻页
            if next_url is not None:
                next_url.click()
            else:
                break
        # 6, 退出
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    dys = DouYu()
    dys.run()