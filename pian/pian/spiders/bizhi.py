import scrapy

from pian.items import PianItem
class BizhiSpider(scrapy.Spider):
    name = 'bizhi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.netbian.com/meinv/']

    def parse(self,response):
        page_num=response.xpath('//*[@id="main"]/div[4]/a[8]/text()').extract_first()
        #获取各个页的网址
        for i in range(5):
            if i+1==1:
                url='http://www.netbian.com/meinv/'
            else:
                url='http://www.netbian.com/meinv/index_%s.htm'%(i+1)
            yield scrapy.Request(url=url,callback=self.parse_page)
    def parse_page(self, response):
        item = PianItem()
        li_list=response.xpath('//div[@class="list"]/ul/li')
        #获取当前页面是第几页
        page=response.xpath('//*[@id="main"]/div[4]/b/text()').extract_first()
        item['mulu']='第%s页'%(page)
        #获取壁纸的原图地址
        for li in li_list:
            try:
                geren_url='http://www.netbian.com'+li.xpath('./a/@href').extract_first()
            except:
                continue
            yield scrapy.Request(url=geren_url, callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        item = response.meta['item']
        #获取图片地址
        img_url=response.xpath('//div[@class="pic"]/p/a/img/@src').extract_first()
        item['url']=img_url
        yield item
