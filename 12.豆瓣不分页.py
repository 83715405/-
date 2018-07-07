import requests
import json


# https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?&start=0&count=18&loc_id=108288
# 准备url
# 发起请求获取 数据

class Douban_movie(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?&start=0&count=18&loc_id=108288"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
            "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288"
        }

    def get_data_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_movies(self, movie_list):
        with open("douban_movie.text", "w")as f:
            for movie in movie_list:
                json.dump(movie, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        data = self.get_data_from_url(self.url).decode()
        movie_list = json.loads(data)["subject_collection_items"]
        print(movie_list)
        self.save_movies(movie_list)


if __name__ == '__main__':
    douban = Douban_movie()
    douban.run()
