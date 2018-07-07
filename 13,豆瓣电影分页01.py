import requests
import json


class DBmovie(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288"
        self.headers = {
            "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288",
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
        }

    def get_data_from_url(self, url, start):
        response = requests.get(url.format(start), headers=self.headers)
        return response.content

    def save_movies(self, movie_list):
        with open("movie.text", "a")as f:
            for movie in movie_list:
                json.dump(movie, f, ensure_ascii=False)
                f.write("\n")

    def get_movie_from_data(self, movie_list_json):
        movie_list = json.loads(movie_list_json)
        start = movie_list["start"]
        total = movie_list["total"]
        count = movie_list["count"]
        next_star = start + count
        if next_star >= total:
            next_star = None
        print(next_star)
        movies = movie_list["subject_collection_items"]
        return movies, next_star

    def run(self):
        start = 0
        while start is not None:
            movie_list_json = self.get_data_from_url(self.url, start).decode()
            movie_list, start = self.get_movie_from_data(movie_list_json)
            self.save_movies(movie_list)


if __name__ == '__main__':
    douban_movie = DBmovie()
    douban_movie.run()
