# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PianItem(scrapy.Item):
    # define the fields for your item here like:
    #图片url
    url=scrapy.Field()
    #图片目录
    mulu=scrapy.Field()
