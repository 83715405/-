import requests
import re
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
# response = requests.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1527253135971_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=风景 高清 唯美&f=3&oq=fengjing &rsp=0&f=3&oq=fengjing &rsp=0", headers=headers)
response = requests.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1527253135971_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A3%8E%E6%99%AF+%E9%AB%98%E6%B8%85+%E5%94%AF%E7%BE%8E&f=3&oq=fengjing+&rsp=0&f=3&oq=fengjing+&rsp=0", headers=headers)
# print(response.content.decode())
img = re.findall(r"^<li.+?</li>", response.content.decode())
print(img)