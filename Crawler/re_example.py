'''

'''
import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36")
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    return html

def get_img(html):
    p = '<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)
    
    '''
    for each in imglist:
        print(each)
    '''
    
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)
        
def get_ip(html):
    p = '(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p, html)
    
    for each in iplist:
        print(each)
        #filename = each.split("/")[-1]
        #urllib.request.urlretrieve(each, filename, None)
    
if __name__ == "__main__":
    # url = "http://tieba.baidu.com/p/3563409202"
    url = "http://www.xicidaili.com/wn/"
    
    # get_img(open_url(url))
    get_ip(open_url(url))