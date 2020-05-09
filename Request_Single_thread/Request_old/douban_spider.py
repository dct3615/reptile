# -*- coding: utf-8 -*-
"""
Created on 2020/1/30 16:37

@author: dct
"""
import json

import requests
# if __name__=='__main__':
#     f=open('basejie.txt','w', encoding="utf-8")
#     Jokelist = getJokeList()
#     for joke in Jokelist:
#         f.writelines(joke)
#         f.writelines('\r\n')
#         f.writelines('~'*100)
#         f.writelines('\r\n')
#     f.close()

def getBooksNum():
    x =requests.get(u'http://www.douban.com/j/tag/items?start=0&limit=1&topic_id=255&topic_name=小说&mod=book'.encode('utf-8'))
    bookjson = x.json()
    booksnum = bookjson['total']
    print(json.dumps(bookjson,indent= 4))

    return booksnum

print(getBooksNum())