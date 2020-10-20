# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from . import settings
import os
# class CrawlProPipeline:
#     def process_item(self, item, spider):
#         return item
class Img_handle(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('爬虫开始')
        return scrapy.Request(item['img_url'],headers={'referer':item['img_ref']},meta={'item':item})
    def file_path(self, request, response=None, info=None):
        item=request.meta.get('item')
        #处理分类文件夹的名字
        title=item.get('img_title')
        i=title.rfind('(')
        floder_name=title[:i]

        source_path=settings.IMAGES_STORE
        #路径
        img_path=os.path.join(source_path,floder_name)
        if not os.path.exists(img_path):
            os.makedirs(img_path)

        url=request.url
        img_name=url.split('/')[-1]
        img_path=os.path.join(floder_name,img_name)
        print(img_path)
        return img_path
    def item_completed(self, results, item, info):
        print('结束')
        return item