import scrapy

from qiubaipro.items import QiubaiproItem
class Test2Spider(scrapy.Spider):
    name = 'test2'
    # allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')
        all_data = []
        for li in li_list:
            name = li.xpath('./div/div/a/span/text()')[0].extract()
            text = li.xpath('./div/a/text()')[0].extract()
            # print(name + ":" + text)
            # dict = {
            #     "name": name,
            #     "text": text
            # }
            # all_data.append(dict)
            item=QiubaiproItem()
            item['name']= name
            item['text']=text
            yield item


