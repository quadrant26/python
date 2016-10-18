# 出错 error
# 
import urllib.error
import urllib.request
from pip._vendor.requests.exceptions import HTTPError

req = urllib.request.Request("http:.//xx-perseus.wang")

try:
	urllib.request.urlopen(req)
except urllib.error.URLError as e:
	print(e.reason)

# HTTPError 300 ~ 399 重定向
# 400 - 499 客户端错误
# 500 ~ 	服务端错误 
 
req = urllib.request.Request("http://perseus.wang/xcvsd.html")
try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.read())

'''
1.
	someurl = "url"
	req = urllib.request.Request(someurl)
	try:
		urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print(e.code)
		print(e.read())
	except urllib.error.URLError as e:
		print(e.reason)
	
2. 推荐
	try:
		urllib.request.Request(someurl)
	except URLError as e:
	if hasattr(e, 'reason'):
		print("We failed to reach a server.')
		print("Reason: ', e.reason)
	elif hasattr(e, 'code'):
		print('The server couldn\'t fulfill the request.')
		print('Error code: ', e.code)
'''