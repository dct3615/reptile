# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 16:05

@author: dct
"""
import requests
from lxml import etree
import re
import csv

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
          }

"""获取每一页中所有电影详细信息的网址"""
def get_movie_urls(base_irl):
    try:
        response = requests.get(base_irl, headers = header,timeout=5)
        text = response.content.decode(encoding='gbk',errors='ignore')
        # print(text)
        html = etree.HTML(text)
    except requests.exceptions.RequestException as e:
        print(e)
    movies_urls = html.xpath("//ul//table[@class='tbspan']//a/@href")
    # movies_urls = ['https://www.ygdy8.net' + m for m in movies_urls]
    movies_urls = map(lambda url:'https://www.ygdy8.net' + url,movies_urls)
    return movies_urls

# url = 'https://www.ygdy8.net/html/gndy/dyzz/20200428/59947.html'
"""解析每一个电影的详细信息"""
def get_movie_details(url):
    movie = {'title':'unkonw', 'poster':'unkonw', 'chinese_movie_name':'unkonw', 'year':'unkonw',
             'English_movie_name':'unkonw','country':'unkonw', 'category':'unkonw', 'lanuage':'unkonw',
             'release_year':'unkonw','douban_score':'unkonw','file_size':'unkonw', 'duration':'unkonw',
             'director':'unkonw', 'leading_role':'unkonw', 'introduction':'unkonw'}
    try:
        response = requests.get(url, headers = header,timeout=5)
        text = response.content.decode(encoding='gbk',errors='ignore')
        html = etree.HTML(text)
    except requests.exceptions.RequestException as e:
        print(e)

    try:
        title = html.xpath("//div[@class='title_all']//font[@color='#07519a']//text()")[0] # 获得标题
        movie['title'] = title # 获取标题
    except:
        print('没找到标题')
    try:
        zoomE = html.xpath('//div[@id="Zoom"]')[0]
    except:
        return False
    try:
        poster = zoomE.xpath('.//img/@src')[0]
        movie['poster'] = poster # 获取海报
    except:
        print("没有海报")
    try:
        movie_details = zoomE.xpath(".//p[1]//text()")
    except:
        return False
    movie_details = [re.sub('\s', ' ', s.strip()) for s in movie_details] # 去除空格
    # print(movie_details)
    for index, movie_detail in enumerate(movie_details):
        if movie_detail.startswith("◎译  名"):
            movie_detail = movie_detail.replace("◎译  名",'').strip()
            movie['chinese_movie_name'] = movie_detail
        elif movie_detail.startswith("◎年  代"):
            year = movie_detail.replace("◎年  代",'').strip()
            movie['year'] = year
        elif movie_detail.startswith("◎片  名"):
            English_movie_name = movie_detail.replace("◎片  名", '').strip()
            movie['English_movie_name'] = English_movie_name
        elif movie_detail.startswith("◎产  地"):
            country = movie_detail.replace("◎产  地", '').strip()
            movie['country'] = country
        elif movie_detail.startswith("◎类  别"):
            category = movie_detail.replace("◎类  别", '').strip()
            movie['category'] = category
        elif movie_detail.startswith("◎语  言"):
            lanuage = movie_detail.replace("◎语  言", '').strip()
            movie['lanuage'] = lanuage
        elif movie_detail.startswith("◎上映日期"):
            release_year = movie_detail.replace("◎上映日期", '').strip()
            movie['release_year'] = release_year
        elif movie_detail.startswith("◎豆瓣评分"):
            douban_score = movie_detail.replace("◎豆瓣评分", '').strip()
            movie['douban_score'] = douban_score
        elif movie_detail.startswith("◎文件大小"):
            file_size = movie_detail.replace("◎文件大小", '').strip()
            movie['file_size'] = file_size
        elif movie_detail.startswith("◎片  长"):
            duration = movie_detail.replace("◎片  长", '').strip()
            movie['duration'] = duration
        elif movie_detail.startswith("◎导  演"):
            director = movie_detail.replace("◎导  演", '').strip()
            movie['director'] = director
        elif movie_detail.startswith("◎主  演"):
            leading_role = []
            leading_role.append(movie_detail.replace("◎主  演", '').strip())
            for x in range(index + 1,len(movie_details)):
                if movie_details[x].startswith('◎标  签'):
                    break
                leading_role.append(movie_details[x].strip())
            movie['leading_role'] = leading_role[0]
        elif movie_detail.startswith("◎简  介"):
            introduction = movie_details[index + 1].strip()
            movie['introduction'] = introduction

    # dowload_url = zoomE.xpath('.//tbody//tr//td//a/@href')[0]
    try:
        dowload_url = zoomE.xpath('.//td[@bgcolor="#fdfddf"]/a/@href')[0]
        movie['dowload_url'] = dowload_url
    except:
        print("未找到下载地址")
        return False
    return movie

def save_moive(movie,count_movie):
    with open('movies.csv', 'a+', encoding='gbk', errors='ignore', newline="") as csv_file:
        writer = csv.writer(csv_file)
        movie['CountMovie'] = count_movie
        if count_movie == 1:
            writer.writerow(movie.keys())
        writer.writerow(movie.values())

def spider_urls(num = 7):
    base_url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    countMovies = 1
    for i in range(1,num + 1,1): # 遍历所有的页码
        base_url = base_url.format(i)# 获取num页电影院网址
        print("正在爬取第{}页".format(i))
        movies_urls = get_movie_urls(base_url)
        for movies_url in movies_urls: # 遍历所有的电影详情
            movie = get_movie_details(movies_url)
            if movie:
                save_moive(movie,countMovies)
                print("已经爬取{}个电影".format(countMovies))
                countMovies += 1

if __name__ == '__main__':
    spider_urls(20)