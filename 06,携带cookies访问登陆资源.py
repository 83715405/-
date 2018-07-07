import requests
# 1,在发送请求headers中携带cookie信息
url = "http://www.renren.com/966129916"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
           "Cookie": "anonymid=jhn6jn0dv08e3n; depovince=GW; _r01_=1; JSESSIONID=abcv7aeOTGuwjajMzVBow; ick_login=8dd47256-ca5f-45bc-b18e-3fd980ae29e9; t=ae76d8815259470735795bd2283630be6; societyguester=ae76d8815259470735795bd2283630be6; id=966129916; xnsid=6441728f; jebecookies=2460dddc-fbf5-46d8-b0b7-090c82887fbb|||||; ver=7.0; loginfrom=null; jebe_key=63ad515d-6bd0-4245-a4e5-4c0635c767a8%7Cfc7eda8fe55b24903b30c9114cd78dd9%7C1527326354533%7C1%7C1527326356471; wp_fold=0"}
response = requests.get(url, headers=headers)
print(response.content.decode())

