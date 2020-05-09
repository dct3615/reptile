# -*- coding: utf-8 -*-
"""
Created on 2020/5/2 20:36

@author: dct
"""
import requests
import re
import os
import time
"""请求网页"""
url_base = 'https://www.vmgirls.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',}
response = requests.get(url_base, headers = headers)
html = response.text

urls = re.findall('<a href="(.*?)" title=".*?" class=".*?" target=".*?">',html)
print(urls)
print(len(urls))

def get_picture(url):
    """发送请求"""
    response = requests.get(url, headers = headers)
    html = response.text
    """解析网页"""
    dir_name = re.findall('<title>(.*?)</title>',html)[-1] # 文件名字
    print(dir_name)
    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html) # 图片地址
    print(urls)
    print(len(urls))
    """保存图片"""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for url in urls:
        # time.sleep(1)
        pic_name = url.split('/')[-1]
        response = requests.get(url, headers=headers)
        path = dir_name + '/' + pic_name
        if not os.path.exists(path):
            print(pic_name)
            with open(path, 'wb') as f:
                f.write(response.content)

for url in urls:
    get_picture(url)