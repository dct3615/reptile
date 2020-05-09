# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from firstscrapy.items import DoubanBookDetilItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'DoubanSpider'
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        item = DoubanBookDetilItem()
        selector = Selector(response)
        books = selector.xpath('//td[@valign="top"  and not(@width)]')
        for eachbook in books:
            title = eachbook.xpath('div[@class="pl2"]/a/text()').extract()
            title = title[0]

            title2 = eachbook.xpath('div[@class="pl2"]/span/text()').extract()
            title2 = title2[0] if len(title2) > 0 else ''
            info = eachbook.xpath('p[@class="pl"]/text()').extract()
            info = info[0]
            rate = eachbook.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
            rate = rate[0]
            hot = eachbook.xpath('div[@class="star clearfix"]/span[@class="pl"]/text()').extract()
            hot = hot[0]
            href = eachbook.xpath('div[@class="pl2"]/a/@href').extract()[0]

            item['title'] = title.strip()
            item['title2'] = title2.strip()
            item['info'] = info.strip()
            item['rate'] = rate.strip()
            item['hot'] = hot.replace(" ", "")
            item['href'] = href
            yield item

        nextlink = selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink = nextlink[0]
            yield Request(nextlink, callback=self.parse)