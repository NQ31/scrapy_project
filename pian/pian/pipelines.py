# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#导入相应的模块
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from . import settings
import os
# class PianPipeline:
#     def process_item(self, item, spider):
#         return item

class PianImgPipeline(ImagesPipeline):
    # 该方法用来对图片url发起请求
    def get_media_requests(self, item, info):
        print('开始下载')
        #在这里需要把item传给file_path方法进行处理。不按图片分页存放的话，可以不写meta参数
        return scrapy.Request(item['url'],meta={'item':item})
    #该方法是用来设置图片的下载路径以及图片的名字
    def file_path(self, request, response=None, info=None):
        item=request.meta['item']
        #分类文件夹，
        wenjianjia=item['mulu']
        '''
        根目录，也就是settings文件下创建的存储图片根目录
        注意：根目录的设置的时候，不要加“./”,否则下面创建文件夹的时候，会自动创建一个根目录名字的文件夹
        '''
        img_source=settings.IMAGES_STORE
        #图片存放的文件夹路径
        img_path = os.path.join(img_source, wenjianjia)
        #判断文件夹存放的位置是否存在，不存在则新建文件夹
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        #更改图片名字
        url=request.url
        url=url.split('/')[-1]
        file_name=url
        #图片存放路径
        image_path=os.path.join(wenjianjia,file_name)
        #返回图片的存放路径

        return image_path
    def item_completed(self, results, item, info):
        print('下载完成')
        return item