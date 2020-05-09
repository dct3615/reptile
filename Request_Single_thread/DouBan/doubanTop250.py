# -*- coding: utf-8 -*-
"""
Created on 2020/5/4 7:59

@author: dct
"""
import requests
from lxml import etree
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
          'Referer': 'https://movie.douban.com/top250?start=0&filter='}

# 获取每个页面电影的网址
def getMovieUrls(baseUrl):
    try:
        response = requests.get(baseUrl, headers = header,timeout=10)
        text = response.text
        # print(text)
        html = etree.HTML(text)
    except requests.exceptions.RequestException as e:
        print(e)
    try:
        movies_urls = html.xpath('//ol[@class="grid_view"]//a/@href')
    except:
        print('获取电影url失败')
    return movies_urls

def getDetail(url):
    try:
        response = requests.get(url, headers = header,timeout=10)
        text = response.text
        html = etree.HTML(text)
    except requests.exceptions.RequestException as e:
        print(e)
    try:
        movie_name = html.xpath('//div[@id="content"]//h1/span/text()')
        movie_sorted = html.xpath('//div[@id="content"]/div[@class ="top250"]/span/text()')
        movies_infos = html.xpath('//div[@id="info"]//text()')
    except:
        print('获取电影详情失败')
        return False
    movie = {}
    p = re.compile(r'[/:]') # 将/:替换为空格
    movies_infos = [re.sub(p,'',movies_info).strip() for movies_info in movies_infos]
    movies_infos = [m for m in movies_infos if m != '']
    movie['movie_name'] = movie_name
    movie['movie_sorted'] = movie_sorted
    movie['movie_name'] = movie_name
    # print(movies_infos)
    for index,movies_info in enumerate(movies_infos):
        if movies_info == '片长':
            movie['片长'] = movies_infos[index + 1]
        elif movies_info == '语言':
            movie['语言'] = movies_infos[index + 1]
    return  movie

def spiderUrls():
    baseUrl = 'https://movie.douban.com/top250?start={}&filter='
    num = 1
    for i in range(0,251,25):
        baseUrl.format(i)
        moveUrls = getMovieUrls(baseUrl)
        for moveUrl in moveUrls:
            movie = getDetail(moveUrl)
            if movie:
                print('第{}电影信息'.format(num))
            else:
                print("获取电影失败")
            num += 1
            print(movie)

if __name__ == '__main__':
    spiderUrls()