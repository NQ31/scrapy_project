# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url=scrapy.Field()
    img_path=scrapy.Field()
    img_referer=scrapy.Field()
    pass
