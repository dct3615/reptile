# -*- coding: utf-8 -*-
"""
Created on 2020/1/15 20:12

@author: dct
"""
class Person():
    pass

class Sheep():
    def __init__(self):
        print("构造函数运行")
    def __new__(cls, *args, **kwargs):
        print('__new__方法')
        return Dog()
    def __del__(self):
        print('析构函数运行')
class Dog():
    def run(self):
        print('dog run')
sheep = Sheep()
print(type(sheep))
sheep.run()

