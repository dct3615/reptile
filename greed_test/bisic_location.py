# -*- coding: utf-8 -*-
"""
Created on 2020/1/12 22:50

@author: dct
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()#内部填写驱动器的路径
#driver.get("https://www.baidu.com")#打开百度浏览器
driver.get("https://www.jd.com")

# search_element = driver.find_element_by_id("key")
# search_element.send_keys("电脑")
# search_element.send_keys(Keys.RETURN)

# driver.implicitly_wait(0.1)#等待0.1s
# driver.find_element_by_class_name('cate_menu_lk').click()
# driver.find_element_by_link_text("手机").click() #保证页面唯一
# driver.find_element_by_partial_link_text("个护").click()
#driver.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]/a[2]').click()
driver.find_element_by_css_selector('#J_cate > ul > li:nth-child(4) > a:nth-child(7)').click()


# time.sleep(5)
# driver.quit()

