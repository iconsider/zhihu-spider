# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.exceptions import DropItem

class ZhihuSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

# 去重pipeline
class DuplicatesPipeline(object):
    def __init__(self):
        self.ids = set()

    def process_item(self, item, spider):
        if item['userId'] in self.ids:
            raise DropItem("发现重复userid (Duplicate item found): %s" % item)
        else:
            self.ids.add(item['userId'])
            return item
        return item

    def close_spider(self, spider):
        print("5秒后关闭浏览器")
        time.sleep(5)
        # 关闭浏览器
        spider.browser.quit();

class savePipeLine(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open("z:/zhihu.txt", 'a') as file:
            file.write(item['userId'] + "\n")