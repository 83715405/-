import requests
import json
import js2py


class RRLogin(object):
    def __init__(self):
        self.login_url = "http://activity.renren.com/livecell/ajax/clog"
        self.rkey_url = "http://activity.renren.com/livecell/rKey"
        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.context = js2py.EvalJs()

    def get_data_from_url(self, url, data=None):
        if data is None:
            response = self.session.get(url)
        else:
            response = self.session.post(url, data=data)
        return response.content

    def load_js_from_url(self, url):
        js = self.get_data_from_url(url).decode()
        self.context.execute(js)

    def run(self):
        # 登陆的url
        rkey_json = self.get_data_from_url(self.rkey_url).decode()
        n = json.loads(rkey_json)["data"]

        self.context.t = {
            "phoneNum": "13215357327",
            "password": "zhai19910228111",
            "c1": 0,
        }
        self.context.n = n
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js")
        js = '''
        t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
                    '''
        self.context.execute(js)
        result = self.get_data_from_url(self.login_url, data=self.context.t.to_dict()).decode()
        print(json.loads(result))
        response = self.session.get("http://activity.renren.com/myprofile")

        with open("my.html","w")as f:
            f.write(response.content.decode())



rrlogin = RRLogin()
rrlogin.run()
