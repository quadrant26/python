# scrapy
'''
1. 创建 1个 scrapy项目
2. 定义 item 容器
3. 编写爬虫
4. 存储内容
'''

'''
scrapy startproject 

cd tutorial

scrapy crawl dmoz

response.xpath('//title/text()').extract()

sel.xpath('//ul/li')
sel.xpath('//ul/li/text()').extract()

sites = sel.xpath("//ul/li")
for site in sites:
	title = site.xpath("a/text()").extract()
	print(title)

scrapy crawl dmoz -o items.json -t json
'''






















