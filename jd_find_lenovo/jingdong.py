# -*- coding: utf-8 -*-
"""
Created on 2020/1/14 20:07

@author: dct
"""
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\00124175\\Desktop\\python\\reptile\\chromedriver.exe')#内部填写驱动器的路径
driver.maximize_window()

def to_goods_page(driver):
    #获取京东首页
    driver.get('https://www.jd.com')
    #定位到电脑
    computer_element = driver.find_element_by_link_text('电脑')

    #鼠标悬停
    ActionChains(driver).move_to_element(computer_element).perform()

    #鼠标点击一下
    driver.implicitly_wait(5)  # 等待单位为秒
    driver.find_element_by_link_text('笔记本').click()

    # 获取当前窗口中的所有句柄
    hanles = driver.window_handles
    # 获取当前窗口的句柄
    index_handle = driver.current_window_handle
    # 句柄切换
    for handle in hanles:
        if handle != index_handle:
            #driver.close()  # 关闭当前浏览器句柄
            driver.switch_to.window(handle)
    #点击thinkpad
    driver.find_element_by_xpath('//*[@id="brand-11518"]/a/img').click()
    #点击7000元以上
    # driver.find_element_by_xpath("//*[@id=\"J_selectorPrice\"]/div/div[2]/div/ul/li[7]/a").click()
    # #点击评论数
    # driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[3]').click()
    #点击第一个电脑
    driver.find_element_by_xpath('//*[@id="plist"]/ul/li[1]/div/div[1]/a/img').click()

    #切换句柄
    current_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != current_handle and handle != index_handle:
            driver.switch_to.window(handle)
    #滚动一下滚动条
    js = "window.scrollTo(0,1000)"
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()

    #定位到所有表格的数据
    driver.implicitly_wait(0.2)  # 等待单位为秒
    info_elements = driver.find_elements_by_class_name('Ptable-item')
    #声明一个变量存储结果数据
    result_list = []
    for info_element in info_elements:
        # 解析商品信息，获取一个字典结构的数据
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
     #保存数据
    save_goods_info(result_list)

def save_goods_info(result_list):
    #声明保存的文件夹
    project_path = os.path.abspath(os.path.curdir)
    file_path = project_path + '/goods_infos/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path + 'computer.infos', 'a', encoding='utf-8') as f:
        f.write(str(result_list))

def get_info_element_dict(info_element):
    #计算机的组成信息
    computer_part = info_element.find_element_by_tag_name('h3')
    #计算机的key，第二列的信息，就是dt
    computer_info_keys = info_element.find_elements_by_tag_name('dt')
    #value， 第三列信息
    computer_info_values = info_element.find_elements_by_xpath('dl//dd[not(contains(@class,"Ptable-tips"))]')

    #声明一个字典存储配置信息
    key_and_value_dict = {}
    #声明一个空字典，用来存储计算机组成信息,最大的类
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

    parts_dict[computer_part.text] = key_and_value_dict

    return parts_dict

if __name__ == '__main__':
    to_goods_page(driver)

