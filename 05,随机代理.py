import requests
import random

# 1, 准备一个代理池
proxies_list = [
    {"http": "123.13.244.219:9999"},
    {"http": "119.28.194.66:8888"},
    {"http": "122.114.31.177:808"},
    {"http": "61.135.217.7:80"},
    {"http": "123.57.217.208:3128"},
    {"http": "218.241.234.48:8080"},
    {"http": "113.87.161.111:808"},
    {"http": "119.5.0.32:808"},
    {"http": "182.99.240.152:61234"},
    {"http": "222.186.45.154:60443"},
]
# 2, 随机选出代理
for i in range(30):
    proxies = random.choice(proxies_list)
    # print(proxies)
    # 3, 使用代理发送请求
    try:
        response = requests.get("http://www.baidu.com", proxies=proxies, timeout=2)
        print(response.status_code)
    except Exception as e:
        print("{}代理不可用".format(proxies))
        proxies_list.remove(proxies)
print(proxies_list)