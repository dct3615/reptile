# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from firstscrapy.items import DoubanBookDetilItem
from urllib.parse import urljoin
from scrapy.utils.response import get_base_url

class DoubanspiderSpider(scrapy.Spider):
    name = 'DoubanBooksDetail'
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        selector = Selector(response)
        books = selector.xpath('//td[@valign="top"  and not(@width)]')
        for eachbook in books:
            title = eachbook.xpath('div[@class="pl2"]/a/text()').extract()[0]
            title2 = eachbook.xpath('div[@class="pl2"]/span/text()').extract()
            title2 = title2[0] if len(title2) > 0 else ''
            info = eachbook.xpath('p[@class="pl"]/text()').extract()[0]
            rate = eachbook.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
            hot = eachbook.xpath('div[@class="star clearfix"]/span[@class="pl"]/text()').extract()[0]
            href = eachbook.xpath('div[@class="pl2"]/a/@href').extract()[0]

            item = DoubanBookDetilItem()
            item['title'] = title.strip()
            item['title2'] = title2.strip()
            item['info'] = info.strip()
            item['rate'] = rate.strip()
            item['hot'] = hot.replace(" ", "")
            item['href'] = href
            item['intr'] = ''
            item['reviews'] = []
            # 请求处理第二个网页，将数据item也传过去

            yield Request(url=href,meta={'book':item},callback=self.parse_bookdetail)
        #检查当前网页是否为最后一页
        nextlink = selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink = nextlink[0]
            yield Request(nextlink, callback=self.parse)

    def parse_bookdetail(self,response):
        selector=Selector(response)
        # 获取书的内容简介
        intrp = selector.xpath('//div[@class="related_info"]/div[@id="link-report"]/div/div[@class="intro"]/p/text()').extract()
        if len(intrp) > 0:
            item=response.meta['book']
            intr='\r\n'.join(intrp)
            item['intr']=intr.lstrip().rstrip()
            yield item

            # baseurl=get_base_url(response)
            # reviewurl=urljoin(baseurl,'reviews') #合并两个链接，书评的地址
            # yield Request(url=reviewurl,meta={'book':item},callback=self.parse_bookreview)

    def parse_bookreview(self, response):
        item = response.meta['book']
        selector = Selector(response)
        # 详细书评的地址
        # reviews = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div[@class="main-bd"]/h2/a/@href').extract()
        # print(reviews)
        # if reviews:
        #     item['reviews'].extend(reviews)
        nextlink = selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink = nextlink[0]
            baseurl = get_base_url(response)
            nextlink = urljoin(baseurl,nextlink) #合并两个链接，书评的地址
            # print('111111111111111',nextlink)
            yield Request(url=nextlink, callback=self.parse_bookreview, meta={'book': item})
        else:
            yield item