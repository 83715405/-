import time
from selenium import webdriver
import json

'''
需求: 列表页面中租房信息的图片url,标题,详情url,价格
1,创建driver对象
2,请求租房的首页
http://sz.58.com/chuzu/
3,通过driver对象解析内容,获取需要的数据
4,保存数据
5,实现翻页
6,退出
'''


class ZuFang(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://sz.58.com/nanshan/hezu/")
    def get_data(self):
        li_s = self.driver.find_elements_by_xpath("/html/body/div[4]/div[1]/div[5]/div[2]/ul/li")[:-2]
        data_li = []
        for li in li_s:
            if li.get_attribute('class') == "apartments-pkg apartments":
                continue
            item = {}
            item["img_url"] = li.find_element_by_xpath("./div[1]/a/img").get_attribute('src')
            print(item)
            item['title'] = li.find_element_by_xpath('./div[2]/h2/a').text

            item['detail_url'] = li.find_element_by_xpath('./div[2]/h2/a').get_attribute('href')
            item['price'] = li.find_element_by_xpath('./div[3]/div[2]').text
            data_li.append(item)
        next_url = self.driver.find_elements_by_partial_link_text('下一页')
        next_page = next_url[0] if len(next_url) != 0 else None
        return data_li, next_page
    def save_data(self, data_list):
        with open("58租房.text", "a", encoding="utf8")as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        while True:
            data_li, url = self.get_data()
            self.save_data(data_li)
            if url is not None:
                url.click()
            else:
                break
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    zfs = ZuFang()
    zfs.run()


