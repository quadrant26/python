'''
一只爬虫的修养

下载一只猫
'''
import urllib.request

# url (placekitten.com)
req = urllib.request.Request("http://placekitten.com/g/500/600")
reponse = urllib.request.urlopen(req)
cat_img = reponse.read()

print(reponse.geturl()) # 返回 url
print(reponse.info()) # 返回 服务器 信息
print(reponse.getcode()) # 返回 http 状态码
with open("cat_500_600.jpg", "wb") as f:
	f.write(cat_img)

