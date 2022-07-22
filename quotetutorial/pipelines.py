# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class QuotetutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017")
        db = self.conn["quotes"]
        self.collection = db["quotes_tb"]

    def process_item(self, item, spider):
        item = dict(item)
        self.collection.insert_one(item)
        return item