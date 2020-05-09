# -*- coding: utf-8 -*-
"""
Created on 2020/1/13 18:31

@author: dct
"""
from selenium import webdriver
import time
import os
import json

driver = webdriver.Chrome()

def login():
    driver.get("https://www.jd.com")
    driver.maximize_window()
    driver.find_element_by_class_name('link-login').click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id('loginname').send_keys('19922619717')
    driver.find_element_by_id('nloginpwd').send_keys('408991dct')
    driver.find_element_by_id('loginsubmit').click()
    save_cookies(driver)

def save_cookies(driver):
    project_path = os.getcwd()
    file_path = project_path + '/cookies/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    cookies = driver.get_cookies()

    with open(file_path + 'jd.cookies', 'w') as c:
        json.dump(cookies, c)
    print(cookies)

def get_url_with_cookies():
    project_path = os.getcwd()
    file_path = project_path + '/cookies/'
    cookies_file = file_path + 'jd.cookies'

    #读取cookies信息
    jd_cookies_file = open(cookies_file, 'r', encoding='utf-8')
    jd_cookies_str = jd_cookies_file.readline()
    #加载cookies信息，转成json格式
    jd_cookies_dict = json.loads(jd_cookies_str)
    print(jd_cookies_dict)

    #清楚旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    #将我们的cookies加入到driver中
    for cookie in jd_cookies_dict:
        print(cookie)
        if 'expiry' in cookie:
            del cookie['expiry']#删除无用的expiry
        driver.add_cookie(cookie)

    driver.get("https://order.jd.com/center/list.action")

#login()
get_url_with_cookies()