# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 15:15
1.目标
​ 爬取豆瓣上显示正在上映的电影的信息，包括电影名、评分、导演、主演等信息。
  将其保存在一个CSV文件中，可以使用Excel打开查看。
2.思路分析
1.获取网页的URL
2.请求网页的源代码
3.解析源代码，提取目标信息
4.保存信息
3.准备工作
1.请求网页源代码使用webdriver.Chrome()
2.解析网页使用xpath

@author: dct
"""
import requests
from lxml import etree

# 1.将目标网站的数据抓取
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
          }
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
response = requests.get(url,headers = header)
text = response.text
# print(response.text)

# 2.数据读取
html = etree.HTML(text)

ul = html.xpath('//ul[@class="lists"]')[1] # 获取正在上映的电影
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title") # 获取标题
    score = li.xpath("@data-score") # 评分
    duration = li.xpath("@data-duration") # 时长
    region = li.xpath("@data-region") # 地区
    poster = li.xpath(".//img/@src") # 海报
    movie = {
        'title':title[0],
        'score':score[0],
        'duration':duration[0],
        'region':region[0],
        'poster':poster[0]
    }
    movies.append(movie)

print(movies)
import pandas as pd

df = pd.DataFrame(movies)
print(df.head())
df.to_csv('movies.csv', encoding='gbk')