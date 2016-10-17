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
import random

url = "http://www.whatismyip.com.tw/"
iplist = ["139.196.108.68:80", "112.81.100.102:8888", "182.90.252.10:2226"]

proxy_support = urllib.request.ProxyHandler({"http" :random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.add_headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

print(html)