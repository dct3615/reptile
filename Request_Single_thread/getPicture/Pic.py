# -*- coding: utf-8 -*-
"""
Created on 2020/5/5 11:26
获取Ajax网址的内容，动态加载
@author: dct
"""
import requests
import re
import os

headers = {
'origin': 'https://www.vmgirls.com',
'referer': 'https://www.vmgirls.com/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}

def save_Imgs(dir_name,urlImgs):
    """保存图片"""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for img in urlImgs:
        # time.sleep(1)
        pic_name = img.split('/')[-1]
        # print(pic_name)
        try:
            print('正在获取图片...')
            response = requests.get(img, headers=headers,timeout = 20)
        except:
            print('获取图片失败')
            continue
        path = dir_name + '/' + pic_name
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(response.content) # 这是一个图片

def get_picture(url):
    """
    :param url: 需要解析的网址（解析最终的网页，获取每个图片的地址）
    :return:
    """
    try:
        # print(url)
        response = requests.get(url, headers = headers,timeout = 5)
        html = response.text
        """解析网页"""
        dir_name = re.findall('<title>(.*?)</title>',html)[-1] # 文件名字
        print(dir_name) # 用于创建文件夹
        urlImgs = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html) # 图片地址
        # print(urlImgs)  # 所有的图片地址
        # print(len(urlImgs))
        save_Imgs(dir_name, urlImgs) # 文件的名字用title，照片的地址传入save_Img
        return True
    except:
        print('网页解析失败')
        return False

def get_pic_urls(url,pages):
    '''
    :param url: 目标网址
    :param pages: 获取多少页
    :return:
    '''
    for page in range(1,pages + 1):
        data = {
            'append': 'list-home',
            'paged': str(page),
            'action': 'ajax_load_posts',
            'page': 'home'
        }
        try:
            response = requests.post(url, headers=headers, data=data, timeout=5)
            html = response.text
            urls = re.findall('<a href="(.*?)" title=".*?" class=".*?" target=".*?">', html)
            # print(urls)
            # print(len(urls))
            yield urls
        except:
            print("获取网页失败")

def spader_img(base_url,pages):
    urlPages = get_pic_urls(base_url, pages)
    for urlpage in urlPages:
        for url in urlpage:
            print('网页解析')
            flag = get_picture(url) # 解析完一个网页打印一次
            if flag:
                print("成功")

if __name__ == "__main__":
    base_url = 'https://www.vmgirls.com/wp-admin/admin-ajax.php'
    spader_img(base_url,20)

