import requests
import json


# 1,准备登陆url
# "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start=0&count=18&loc_id=108288"
# 2,发送请求, 解析数据
# 3,分页功能实现


class DouB(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start={}&count=18&loc_id=108288"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36Query String Parametersview sourceview URL encoded",
            "Referer": "https://m.douban.com/tv/american"
        }

    def get_data_from_url(self, url, start):
        response = requests.get(url.format(start), headers=self.headers)
        return response.content

    def get_movie_from_json(self, movie_json):
        dic = json.loads(movie_json)

        movie_list = dic["subject_collection_items"]
        return movie_list

    def save_movies(self, movie_list):
        with open("美剧.text", "a")as f:
            for movie in movie_list:
                json.dump(movie, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        start = 0
        while True:
            movie_json = self.get_data_from_url(self.url, start).decode()
            movie_list = self.get_movie_from_json(movie_json)
            self.save_movies(movie_list)
            start += 18
            if len(movie_list) == 0:
                break


if __name__ == '__main__':
    doub = DouB()
    doub.run()
