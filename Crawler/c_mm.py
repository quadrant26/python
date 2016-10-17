import urllib.request
import os
import os.path
import random

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
	'''
	proxylist = ["122.96.59.104:80", "60.194.100.51:80", "123.56.74.13:8080", "119.6.136.122:80", "122.96.59.106:80", "221.226.82.130:8998", "121.40.108.76:80"]
	proxyip = random.choice(proxylist)
	proxy_support = urllib.request.ProxyHandler({"http" : proxyip})
	proxy_opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(proxy_opener)
	'''
	response = urllib.request.urlopen(req)
	html = response.read()
	
	return html


def get_pages(url):
	html = url_open(url).decode("utf-8")
	
	a = html.find("current-comment-page") + 23
	b = html.find("]", a)

	return html[a:b]

def find_imgs(url):
	html = url_open(url).decode("utf-8")
	img_adds = []
	a = html.find('img src=')
	
	while a != -1:
		b = html.find(".jpg", a, a+100)
		# 不是 jpg 返回 -1
		if b != -1:
			img_adds.append(html[a+9:b+4])
		else:
			b = a + 9
			
		a = html.find("img src=", b)
		
	return img_adds
		

def save_imgs(folder, img_adds):
	for each in img_adds:
		filename = each.split("/")[-1]
		with open(filename, 'wb') as f:
			img = url_open(each)
			f.write(img)

def download_mm(folder='J:\pmm\mm', pages=10):
	'''
	if not os.path.isdir(folder):
		os.mkdir(folder)
		os.chdir(folder)
	else:
		os.chdir(folder)
    '''
	try:
		os.mkdir(folder)
		os.chdir(folder)
	except:
		os.chdir(folder)
		
	url = "http://jiandan.net/ooxx/"
	page_num = int(get_pages(url))
	
	
	page_url = url + 'page-' + str(page_num) + "#comments"
	img_adds = find_imgs(page_url)
	
	save_imgs(folder, img_adds)
	
	'''
	for i in range(pages):
		page_num -= i
		page_url = url + 'page-' + str(page_num) + "#comments"
		img_adds = find_imgs(page_url)
		save_imgs(folder, img_adds)
	'''

if __name__ == "__main__":
	download_mm()
