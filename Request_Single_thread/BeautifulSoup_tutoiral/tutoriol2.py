# -*- coding: utf-8 -*-
"""
Created on 2020/5/4 17:17

@author: dct
"""

from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
soup = BeautifulSoup(html,"lxml")

"""
功能概述
1、获取所有的"a"标签
2、获取第二个"a"标签
3、获取class=bri的a标签
4、获取id=u1,class=bri的a标签
5、获取所有a标签的href属性
"""

# 1、获取所有的"a"标签
a_s = soup.find_all('a')
print('================1==============')
for a in a_s:
    print(a)
    print(type(a))
    print('=============2===================')
    break

# 2、获取第二个"a"标签
a_s = soup.find_all('a',limit=2)[1] # 最多两个
print(a_s)
print('===============3=================')

# 3、获取class=bri的a标签
# a_s = soup.find_all('a',class_='bri')
a_s = soup.find_all('a',attrs={'class' : 'bri'})
print(a_s)

# 4、获取id=test,class=test的a标签
a_s = soup.find_all('a',class_='test',id = 'test')
a_s = soup.find_all('a',attrs={'class' : 'test','id' : 'test'})

# 5、获取所有a标签的href属性
alists = soup.find_all('a')
# for alist in alists:
    # 通过下标
    # href = alist['href']
    # 通过attrs属性
    # href = alist.attrs['href']
    # print(href)

# 6、获取文字
# a_s = soup.find_all("a")
# for a in a_s:
#     # text = a[0].string
#     # print(text)
#     a.strings
print('===================================')
u1 = soup.find_all('div', id = 'u1')
print(u1)
print(u1.strings)
print(u1.stripped_strings)


