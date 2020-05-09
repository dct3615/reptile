# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html




import pymysql

class MySQLDoubanBookPipline(object):
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',
                           passwd='123456',db='douban_testdb',charset='utf8')
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()# 得到一个可以执行SQL语句的光标对象

    def process_item(self,item,spider):
        # 如果使用第一个爬虫，需要删除 intr
        sql='insert into doubanbook(title,title2,rate,hot,intr,info,reviews) values (%s,%s,%s,%s,%s,%s,%s)'
        bookinfo=[item['title'],item['title2'],item['rate'],item['hot'],item['intr'],item['info'],item['reviews']]
        self.cursor.execute(sql,bookinfo) # 执行SQL语句
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()