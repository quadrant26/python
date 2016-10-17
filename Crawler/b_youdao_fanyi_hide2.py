'''
一只爬虫的修养

有道词典 翻译

one:
	urllib.request.Request(url, data, heads)
	heads = {}

two:
	urllib.request.Request(url, data)
	Request.add_header(key, val)

多次访问解决访问：
	1. 利用 time.sleep() 休眠
	2. 代理
		1. {"类型" : "代理ip:端口号"}
			proxy_support = urllib.request.ProxyHandler({})
		2. 定制 opener
			opener = urllib.request.build_opener(proxy_support)
		3. 
		 a: 安装 opener
			urllib,request.install_opener(opener)
		 b: 调用 open
		 	opener.open(url)


'''
import urllib.request
import urllib.parse
import json
import time

while True:
	content = input("请输入需要翻译的内容：")
	if content == '!q':
		print("退出程序")
		break

	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=u"

	'''
	head = {}
	head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
	'''

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

	# req = urllib.request.request(url, data)
	req = urllib.request.request(url, data, head)
	req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
	html = req.read().decode("utf-8")

	target = json.loads(html)
	# print(target['translateResult'][0][0])
	# print(target['translateResult'][0][0]['tgt'])

	print("翻译的结果为： %s" % (target['translateResult'][0][0]['tgt']))

	time.sleep(5)
