# -*- coding: utf-8 -*-
"""
Created on 2020/1/13 17:39

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
driver.implicitly_wait(5)#等待5s
old_phone = driver.find_element_by_link_text('老人机')
old_phone.click()
#获取当前窗口中的所有句柄，这里获取的句柄个数为2
hanles = driver.window_handles
#获取当前窗口的句柄
current_handle = driver.current_window_handle
#句柄切换
for handle in hanles:
    if handle != current_handle:
        driver.close()#关闭当前浏览器句柄
        #driver.quit()#关闭整个浏览器
        driver.switch_to.window(handle)
        #driver.save_screenshot('old_phone.jpg')#有警告，因为默认截图png
        driver.save_screenshot('old_phone.png')





