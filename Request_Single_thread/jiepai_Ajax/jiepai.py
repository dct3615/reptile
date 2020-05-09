# -*- coding: utf-8 -*-
"""
Created on 2020/5/4 11:04
失败，改天学会了回头再弄
@author: dct
"""
import json
from bs4 import BeautifulSoup
import requests
from lxml import etree
from requests.exceptions import RequestException
import re
# 将存入的字典参数编码为URL查询字符串，即转换成以key1=value1&key2=value2的形式
from urllib.parse import urlencode

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    "x-requested-with": "XMLHttpRequest",
    'cookie': 'tt_webid=6822818667600987662; s_v_web_id=verify_k9rwd9qm_SqsH5B1b_UJ2w_4W3H_8jO7_JmG9plmxlJSv; ttcid=1fab35350b6743fcaf5640d97bb7588310; WEATHER_CITY=%E5%8C%97%E4%BA%AC; SLARDAR_WEB_ID=9982a72b-ff7f-433e-b065-43f8aeb8697f; tt_webid=6822818667600987662; csrftoken=e274c1a3e54827e33327d6a4d8ba0bbf; passport_csrf_token=d878e64fe9db3abcfcb54e8c60662ac5; __tasessionId=ygj6y6q2b1588565168219; sso_auth_status=2717d7baec8caff2054622b682750c25; sso_uid_tt=8179486a44d9dd0ff6a362043acd2909; sso_uid_tt_ss=8179486a44d9dd0ff6a362043acd2909; toutiao_sso_user=f84ec5751ba0ae6321454a6412998ef9; toutiao_sso_user_ss=f84ec5751ba0ae6321454a6412998ef9; passport_auth_status=4652e5b0f6aa2be153116df93929400b%2C94c4cc034685a4328142d9765cff7c02; sid_guard=858369810ad81467cffc07698824445a%7C1588565200%7C5184000%7CFri%2C+03-Jul-2020+04%3A06%3A40+GMT; uid_tt=e81ec679f3dea08ddef62162576ee06b; uid_tt_ss=e81ec679f3dea08ddef62162576ee06b; sid_tt=858369810ad81467cffc07698824445a; sessionid=858369810ad81467cffc07698824445a; sessionid_ss=858369810ad81467cffc07698824445a; tt_scid=Ilszr3310V7PZ2QemiLQcQP9ECMfsrjeRe.abSi4DJBsUJ04wnf1q.wOgCIdNARMb7d8'
}

def get_page_index(offset, keyword):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab ': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers = header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None
def parse_page_index(html):
    html_data = json.loads(html) # 将json数据转化为字典
    if html_data and 'data' in html_data.keys():
        for item in html_data.get('data'): # data.get('data')是一个列表，遍历列表
            yield item.get('article_url')# item是字典
def get_detail_page(url):
    try:
        response = requests.get(url,headers = header)
        if response.status_code == 200:
            return response.content.decode(encoding='utf-8',errors='ignore')
        return None
    except RequestException:
        print('请求出错')
        return None
def parse_page_detail(html):
    # soup = BeautifulSoup(html, 'lxml')
    # title = soup.select('title')[0].get_text()
    htmlE = etree.HTML(html)
    title = htmlE.xpath('//title/text()')[0]
    print(title)
    # with open('test.html','w',encoding='utf-8') as f:
    #     f.write(html)
    # print(html)
    result = re.findall(r'(http:\\u002F:.*)&quot; img_width&#x3D',html)
    print(len(result),result)
def main():
    html = get_page_index(0, '街拍')
    # print(html)
    for url in parse_page_index(html):
        # print(url)
        if url:
            print(url)
            html = get_detail_page(url)
            if html:
                parse_page_detail(html)
            break

if __name__ == '__main__':
    main()