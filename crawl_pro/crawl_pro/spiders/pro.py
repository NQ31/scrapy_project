import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawl_pro.items import CrawlProItem

class ProSpider(CrawlSpider):
    name = 'pro'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.mzitu.com/']
    # https://www.mzitu.com/217755
    #链接提取器，将主链接页面提取的链接发起请求，并将请求结果交给parse_item处理
    #妹子图个人图集链接
    link_meizi=LinkExtractor(allow=r'https://www.mzitu.com/\d+')

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_item', follow=True),
        Rule(link_meizi,callback='parse_person',follow=True),
        # Rule(link_tuji_page, callback='parse_img', follow=True)
    )

    def parse_item(self, response):
        item = {}
        li_list=response.xpath('//*[@id="pins"]/li')
        for li in li_list:

            # num=li.xpath('./span[1]/text()').extract_first()
            tji_url=li.xpath('./span[1]/a/@href').extract_first()
            title=li.xpath('./span[1]/a/text()').extract_first()
            # print(title,tji_url)

    def parse_person(self,response):
        item =CrawlProItem()
        img_title=response.xpath('/html/body/div[2]/div[1]/h2/text()').extract_first()
        img_referer=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/@href').extract_first()
        img_url=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract_first()

        item['img_url']=img_url
        item['img_ref']=img_referer
        item['img_title']=img_title

        yield item

    # def parse_img(self,response):
    #     img_url=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract_first()
    #     print(img_url)