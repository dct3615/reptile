# -*- coding: utf-8 -*-
"""
Created on 2020/1/13 17:29

@author: dct
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time

driver = webdriver.Chrome()#内部填写驱动器的路径
#driver.get("https://www.baidu.com")#打开百度浏览器
driver.get("https://www.jd.com")

elem = driver.find_element_by_link_text('手机')
ActionChains(driver).move_to_element(elem).perform()#鼠标移动
time.sleep(5)

old_phone = driver.find_element_by_link_text('老人机')
old_phone.click()







