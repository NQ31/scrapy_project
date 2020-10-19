# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    def __init__(self):
        self.fp=None
    def open_spider(self,spider):
        print('start')
        self.fp=open('./data.txt','w')
    def process_item(self, item, spider):
        self.fp.write(item['name']+":"+item['text']+'\n')
        print(item)
        return item
    def close_spider(self,spider):
        self.fp.close()
        print('end')

class QiubaiproPipeline_db:
    conn=None
    cursor=None
    def open_spider(self,spider):
        print('mysql start')
        self.conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='root',db='lufei')
    def process_item(self, item, spider):
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item['name'],item['text']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()