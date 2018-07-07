import json

str1 = '{"name": "python", "age":18, "gender":false,"to_do":"跳舞"}'
dic = json.loads(str1)
print(dic, type(dic))

str2 = json.dumps(dic, ensure_ascii=False, indent=4)
print(str2, type(str2))

with open("123.json", "w", encoding="utf8")as f:
    json.dump(dic, f, ensure_ascii=False, indent=4)
with open("123.json", "r")as f:
    dic2 = json.load(f)
    print(dic2, type(dic2))