import re
regex = re.compile('\d+')

rs = regex.findall("a\db1cd1\n23acd")
print(rs)
rs = regex.sub("_","a\db1cd1\n23acd")
print(rs)