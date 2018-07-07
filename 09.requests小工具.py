import requests

response = requests.get("http://www.baidu.com?wd=python")

print(response.cookies)
# response接受的的cookies为cookiejar格式,转化为字典要用dict_from_cookie_jar
print(requests.utils.dict_from_cookiejar(response.cookies))

dic = requests.utils.dict_from_cookiejar(response.cookies)
# 页可以用cookiejar_from_dict把字典转化为cookiejar格式
print(requests.utils.cookiejar_from_dict(dic))

print(response.url)
# 对url进行编码
print(requests.utils.quote(response.url))
url = requests.utils.quote(response.url)
# 对url解码
print(requests.utils.unquote(url))

# requests请求https协议的网站的时候默认开始ssl的验证,有些网站使用的证书不是默认的证书
# 这个时候我们要把安全认证证书关闭

response = requests.get("http://www.12306.cn/mormhweb", verify=False)
print(response.content.decode())