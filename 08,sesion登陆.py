import requests

# 1,获取session'对象
session = requests.session()
login_url = "http://www.renren.com/PLogin.do"
ind_url = "http://www.renren.com/966130653/profile"
session.headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
# 2, 登陆
data = {
    "email": "13215357327",
    "password": "zhai19910228111",
}
# 3,使用session对象发送登陆请求
response = session.post(login_url, data=data)
with open("home.html", "wb") as f:
    f.write(response.content)
# 4,使用session访问请求资源
response = session.get(ind_url, data=data)
with open ("profile.html", "wb") as f:
    f.write(response.content)
