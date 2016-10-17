'''
一只爬虫的修养
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False)
'''
import urllib.request
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8")
print(html)
