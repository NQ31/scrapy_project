import scrapy
from mzitu.items import MzituItem

class MziSpider(scrapy.Spider):
    name = 'mzi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.mzitu.com/']
    #第几页
    def parse(self, response):
        page_num=response.xpath('/html/body/div[2]/div[1]/div[3]/div/a[4]/text()').extract_first()
        for i in range(0,4):
            if i+1==1:
                url='https://www.mzitu.com/'
            else:
                url='https://www.mzitu.com/page/%s/'%(i+1)
            # print('第%s页 --'%i,url)
            yield scrapy.Request(url=url,callback=self.page_parse,meta={'ref':url})
    #获取各个图集url
    def page_parse(self,response):

        fef=response.meta['ref']
        li_list=response.xpath('//div[@class="postlist"]/ul/li')
        for li in li_list[0:10]:
            tuji_url=li.xpath('./a/@href').extract_first()
            tuji_title=li.xpath('./span[1]/a/text()').extract_first()
            yield scrapy.Request(url=tuji_url,headers={'referer':fef},callback=self.tuji_parse,meta={'tuji_url':tuji_url,'ref':tuji_url})
    #获取每个图集的页数
    def tuji_parse(self,response):
        item=MzituItem()
        ref=response.meta['ref']
        tuji_url=response.meta['tuji_url']
        tuji_page_num=response.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()').extract_first()
        for i in range(int(tuji_page_num)):
            if i+1==1:
                url=tuji_url
            else:
                url=tuji_url+'/%s'%(i+1)
            item['img_referer']=url
            # print('图集第%s页 -url--'%i,url)
            yield scrapy.Request(url=url,headers={'referer':ref},callback=self.img_parse,meta={'item':item})
    #下载图集的图片
    def img_parse(self,response):
        item=response.meta['item']
        img_url=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract_first()
        img_path=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@alt').extract_first()
        item['img_path']=img_path
        # print(img_url)
        item['img_url']=img_url
        # print(item['img_url'])
        # print(item['img_path'])
        yield item



