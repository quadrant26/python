import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	];

	'''
	def parse(self, response):
		filename = response.url.split("")[-2]
		with open(filename, "wb") as f:
			f.write(response.body)
	'''

	def parse(self, response):
		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//ul[@class="directory-url"]/li').extract()
		for site in sites:
			'''
			item = DmozItem()
			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href ').extract()
			desc = site.xpath('text()').extract()
			print(title, link, desc)
			'''
			item = DmozItem()
			item['title'] = site.xpath('a/text()').extract()
			item['link'] = site.xpath('a/@href ').extract()
			item['desc'] = site.xpath('text()').extract()
			items.append(item)
			
			return items