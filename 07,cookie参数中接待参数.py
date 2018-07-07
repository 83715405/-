import requests

# 1,在发送请求headers中携带cookie信息
url = "http://www.renren.com/966130653/profile"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
cookies_str = "anonymid=jhn6jn0dv08e3n; depovince=GW; _r01_=1; JSESSIONID=abcv7aeOTGuwjajMzVBow; wp=1; ick=7c7db7ef-e4b6-4c51-83c4-82ee2a59f30a; XNESSESSIONID=7ac63edacfa1; WebOnLineNotice_966130653=1; jebe_key=63ad515d-6bd0-4245-a4e5-4c0635c767a8%7Cabb3bf94774e3331ed494363025377d0%7C1527329916240%7C1%7C1527329918207; jebecookies=a3b3887d-5067-4c4a-818c-8ce6c5d0f14d|||||; ick_login=8dd47256-ca5f-45bc-b18e-3fd980ae29e9; _de=4B68F526C098323A1A18C863E5B80304; p=5f879ff1573f5e20c5c4b0b6fb80708f3; first_login_flag=1; ln_uact=13215357327; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a5db6545d3d64681114028dcd268e1393; societyguester=a5db6545d3d64681114028dcd268e1393; id=966130653; xnsid=640ab52c; loginfrom=syshome; ch_id=10016; wp_fold=0"
cookies = {cookie_str.split("=")[0]:cookie_str.split("=")[1] for cookie_str in cookies_str.split("; ")}
print(cookies)
response = requests.get(url, headers=headers, cookies=cookies)
print(response.status_code)
print(response.content.decode())
