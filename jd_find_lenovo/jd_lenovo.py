# -*- coding: utf-8 -*-
"""
Created on 2020/1/14 19:22

@author: dct
"""


from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\00124175\\Desktop\\python\\reptile\\chromedriver.exe')#内部填写驱动器的路径

def large_sale_leo():
    driver.maximize_window()
    driver.get("https://www.jd.com")
    driver.implicitly_wait(0.1)  # 等待单位为秒
    leo_element = driver.find_element_by_id('key')
    leo_element.send_keys('联想')
    leo_element.send_keys(Keys.ENTER)

    sal_element = driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]/span')
    driver.implicitly_wait(0.1)  # 等待单位为秒
    sal_element.click()
    driver.implicitly_wait(0.2)  # 等待单位为秒
    large_sal_element = driver.find_element_by_class_name('p-tag3')
    large_sal_element.click()

    driver.implicitly_wait(2)  # 等待单位为秒
    style_element = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div[1]/ul/li[2]')
    style_element.click()


large_sale_leo()
