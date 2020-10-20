import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ProSpider(CrawlSpider):
    name = 'pro'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']
    #链接提取器，将主链接页面提取的链接发起请求，并将请求结果交给parse_item处理
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
