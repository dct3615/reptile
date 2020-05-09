# -*- coding: utf-8 -*-
"""
Created on 2020/5/5 10:10
破解有道翻译的加密
@author: dct
"""
import hashlib
import time
import random
import requests

def make_md5(string: str):
    '''
    产生md5
    :param string
    :return:md5
    '''
    string = string.encode('utf-8') # 编码
    md5 = hashlib.md5(string).hexdigest() # 返回摘要，是一个32位的字符串
    return md5

def youdao(string:str):

    e = string

    r = str(round(time.time()*1000))# 一共13位
    salt = r + str(random.randint(0,9)) # [0,9]
    ts = r
    bv = make_md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    sign = make_md5('fanyideskweb' + e + salt + 'Nw(nmmbP%A-r6U3EUn]Aj')


    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    '''待传递的值'''
    data = {
        'i': e, # 翻译的值
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    headers = {
    'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.top',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '255',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'P_INFO=dct3615@163.com|1579046871|0|other|00&14|bej&1577670119&other#bej&null#10#0#0|175706&0||dct3615@163.com; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-661882519@118.198.248.101; JSESSIONID=abcmUFWgoJR0d_aSNyIhx; OUTFOX_SEARCH_USER_ID_NCOO=538402220.5937054; _ntes_nnid=e71c27e0be7f1313dcf4dd2d95b3d145,1588641045029; ___rl__test__cookies=1588641085870',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'X-Requested-With': 'XMLHttpRequest'
    }

    # 构造请求
    response = requests.post(url,headers = headers,data=data)
    print(response.text)

if __name__ == "__main__":
    while True:
        string = input('输入你要翻译的内容')
        if string == '***':
            break
        youdao(string)
