# -*- coding: utf-8 -*-
"""
Created on 2020/5/4 19:43
获取音乐的热门评论，参数加密，暂时还不会做
@author: dct
"""
import json

import requests

def parse_comments_url(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
               'referer':'https://music.163.com/song?id=4466775'}
    data = {'params': 'LeTSk9AOd2BB1Qvf46HmWJ1bqN6XHSaSLuquzXl6/HByRLfgYc/XJPjZMQtGt3UkpsV5dM7UOwNWLzHAqHEUsTA1P7GB6BLUeNnqpvGxfoJuefztSFg4o+hNoXdPa+H5rhiJ6cXQyuWLczo86YlcW4i7qPr1NYgCfAdPFLnP5lUeCoSXnQSYtxr7sYQHfTgh',
            'encSecKey': '372698bda156f84eabcd7458e1df961a724eee95d8333030ef7f3dcb201bd9340632f823472015d83c27e89a7da5b76cc4c081d930860453d95e3d83f4bbfc152644edfbaa875ff5baeeeb44829c63847ab2cf045eec822b684e6f1066d5c015fa3557ab3950f432cbae3b9ebad1c4984f8ba42943607a12e193ef536f27d18f'}

    response = requests.post(url,headers = headers,data=data)
    text = json.loads(response.text) # 转化为字典
    comments = text.get('hotComments') # comments,hotComments
    for comment in comments:
        text = comment.get('content')
        print(text)

def main():
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_4466775?csrf_token='
    parse_comments_url(url)

if __name__ == "__main__":
    main()