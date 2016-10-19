'''
URL 管理器
网页下载器 （urllib2 requests）
网页解析器    -> (价值数据)

urllib2
1.
    urlopen()
    getcode()
    read()
2. 
    request = Request()
    request.add_data()
    request.add_header()
    
    data()
    header()
    
3. 特殊
    HTTPCookieProcessor
    ProxyHanler
    HTTPHandler
    HTTPRedirectHandler
    
    opener = build_opener()
    open = installs_opener(opener)
    
    HTTPCookieProcessor
        cj = cookielib.CookieJar()
        opener = bulid_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        urllib2.urlopen(url)
    
BeautufulSoup
    
    
内存
mysql
Redis

'''
