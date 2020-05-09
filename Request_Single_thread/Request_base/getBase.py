# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 8:50

@author: dct
"""
import requests

url = 'https://book.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',}

"""获取 get 请求"""
response = requests.get(url,headers = headers)
# print(type(response.text))
# print(response.text) # 解码后的数据（根据自己的猜想解码，有时候会猜测错误）

# print(type(response.content))
# print(response.content.decode('utf-8')) # 将原始数据自己解码

# print(response.url) # 请求的网址
# print(response.encoding) # 编码方式
# print(response.status_code) # 响应状态码

params = {
    'wd' : '董传亭'
}
# 相当于百度搜索 "中国"
response = requests.get("https://www.baidu.com",params = params, headers = headers)
with open("baidu.html",'w',encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))
# print(response.url)