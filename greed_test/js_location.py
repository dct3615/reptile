# -*- coding: utf-8 -*-
"""
Created on 2020/1/13 20:38

@author: dct
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time

def search_12306():
    driver = webdriver.Chrome()  # 内部填写驱动器的路径
    driver.get("https://www.12306.cn/index")
    driver.implicitly_wait(0.1)  # 等待0.1s
    fro_sta = driver.find_element_by_id('fromStationText')
    time.sleep(2)
    fro_sta.click()
    time.sleep(2)
    fro_sta.send_keys('北京')#下拉选择北京北，右击检查可以看代码
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='北京北']").click() #//代表任意目录，*代表所有

    to_sta = driver.find_element_by_id('toStationText')
    time.sleep(2)
    to_sta.click()
    time.sleep(2)
    to_sta.send_keys('长春')
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='citem_0']").click()#任意标签下的：id=citem_0

    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    date_element = driver.find_element_by_id('train_date')
    time.sleep(2)
    date_element.click()
    time.sleep(2)
    date_element.clear()
    date_element.send_keys('2020-01-15')
    time.sleep(2)
    driver.find_element_by_class_name('form-label').click()
    time.sleep(2)
    driver.find_element_by_id('search_one').click()
    time.sleep(5)



search_12306()