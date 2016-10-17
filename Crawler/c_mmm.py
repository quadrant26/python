import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_totalpages(url):                          #通过版块地址获得该版块所有页数（每页有50个系列），返回值为数字
    html = url_open(url).decode('gbk')
    reg = r'共 <strong>(.*?)</strong>页'
    totalpages = re.findall(reg,html)[0]
    return int(totalpages)

def get_sercoverurl(pageurl):                    #通过页面地址获得该页面下所有系列的封面地址，返回值为列表
    html = url_open(pageurl).decode('gbk')
    reg = r'<p><a href="(.*?)"'
    sercoverurl = re.findall(reg, html)
    return sercoverurl                          #各个系列的封面 列表

def get_serurl(sercoverurl):                  #通过封面获得该系列的所有图片所在的页面地址 (每个页面有一张图片，其地址待下一步获取)
    html = url_open(sercoverurl).decode('gbk')   #
    reg1 = r'<li><a>共(.*?)页'
    totalsheets = int(re.findall(reg1, html)[0])  # 获得该系列图片总张数
    serurls = []
    serurls.append(sercoverurl)
    for eachsheet in range(2,totalsheets+1):
        serurl = sercoverurl[:-5] + '_' + str(eachsheet) + sercoverurl[-5:]
        serurls.append(serurl)
    return serurls

def get_picurl(serurl):
    html = url_open(serurl).decode('gbk')
    reg = r"<img src='(.*?)'"
    picurl = re.findall(reg,html)[0]

    return picurl     #只有一个地址，即封面地址

def download_cl(folder = 'J:\pmm\爬虫youmzi'):               #主程序
    try:
        os.mkdir(folder)
        os.chdir(folder)
    except:
        os.chdir(folder)
    url = 'http://www.youmzi.com/meinv.html'
    totalpages = get_totalpages(url)
    print(totalpages)
    for eachpage in range(1,totalpages+1):
        pageurl = url[:-5] + '_'+ str(eachpage) + url[-5:]
        print(pageurl)
        sercoverurl = get_sercoverurl(pageurl)       #获得系列的封面地址 列表
        print(sercoverurl)
        for eachsercover in sercoverurl:
            serurl = get_serurl(eachsercover)      #返回系列的所有地址 列表
            for oneser in serurl:
                picurl = get_picurl(oneser)
                print(picurl)
                filename = picurl.split('/')[-1]
                urllib.request.urlretrieve(picurl, filename)

if __name__ == '__main__':
    download_cl()