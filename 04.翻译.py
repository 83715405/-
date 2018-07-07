import requests

# url = "http://httpbin.org/post"
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1Name"}
# data = {
#     "name": "laowang "
# }
# response = requests.post(url, data=data, headers=headers)
# print(response.content.decode())

url = "http://fanyi.baidu.com/basetrans"
data ={
    "from": "zh",
    "to": "en",
     "query": "你好"
}
response = requests.post(url, data=data, headers=headers)
print(response.content.decode())