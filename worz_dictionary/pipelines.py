# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3


class WorzDictionaryPipeline(object):
    """
    this pipeline takes item from from spider
    every dictionary source will creates a new sqllite database
    >> parse item html
    >> save item into database
    """
    def process_item(self, item, spider):
        """
        {TODO} save it into db
        db_filename = '{0}.db'.format(item.source)
        db_is_new = not os.path.exists(db_filename)
        conn = sqlite3.connect(db_filename)
        """
        return item
