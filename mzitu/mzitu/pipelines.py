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
# class MzituPipeline:
#     def process_item(self, item, spider):
#         return item
class myPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('下载开始')
        return scrapy.Request(item['img_url'],headers={'referer':item['img_referer']},meta={'item':item})
    def file_path(self, request, response=None, info=None):
        item=request.meta['item']
        #获取目录
        floder=item['img_path']
        source_path=settings.IMAGES_STORE
        #路径
        img_path=os.path.join(source_path,floder)
        if not os.path.exists(img_path):
            os.makedirs(img_path)

        url = request.url
        url = url.split('/')[-1]
        img_name=url
        img_file_path=os.path.join(floder,img_name)
        print(img_file_path)

        return img_file_path
    def item_completed(self, results, item, info):
        print('下载结束')
        return item