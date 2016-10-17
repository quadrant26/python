'''
一只爬虫的修养

有道词典 翻译
'''
import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=u"
data = {}
data['type'] = 'AUTO'
data["i"] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode("utf-8")

response = urllib.request.urlopen(url, data)
html = response.read().decode("utf-8")

target = json.loads(html)
# print(target['translateResult'][0][0])
# print(target['translateResult'][0][0]['tgt'])

print("翻译的结果为： %s" % (target['translateResult'][0][0]['tgt']))
