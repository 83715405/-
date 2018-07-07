import json
import js2py
import requests


class RRlogin(object):
    def __init__(self):
        self.rkey_url = "http://activity.renren.com/livecell/rKey"
        self.clog_url = "http://activity.renren.com/livecell/ajax/clog"
        self.session = requests.session()
        self.session.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
                                "X-Requested-With": "XMLHttpRequest",
                                "Content-Type": "application/x-www-form-urlencoded",
                                }
        self.context = js2py.EvalJs()
    def get_dat_from_url(self,url, data=None):
        if data is None:
            response = self.session.get(url)
        else:
            response = self.session.post(url, data=data)
        return response.content
    def load_js_from_url(self,url):
        js = self.get_dat_from_url(url).decode()
        return self.context.execute(js)
    def run(self):
        data = self.get_dat_from_url(self.rkey_url).decode()
        data_dic = json.loads(data)["data"]

        self.context.t = {
            "phoneNum": "13215357327",
            "password": "zhai19910228111",
            "c1": 0,
            # "rKey": data_dic["rkey"]
        }
        self.context.n = data_dic
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js")
        js = '''t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey'''

        self.context.execute(js)
        result = self.get_dat_from_url(self.clog_url, data=self.context.t.to_dict())
        print(result)
        fdata = self.get_dat_from_url("http://activity.renren.com/myprofile").decode()
        print(fdata)
if __name__ == '__main__':
    renren_login = RRlogin()
    renren_login.run()