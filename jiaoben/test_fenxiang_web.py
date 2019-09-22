#!/usr/bin/python
#-*-cod:utf-8-*-
from selenium import webdriver
import pytest
import allure
import yaml


# dr=webdriver.Chrome    #指定浏览器
# dr.get('https://www.fxiaoke.com')
# print(dr.title)
# with open(file=r'E:\ruanjianceshi\纷享销客\element\fen.yaml',mode='r',encoding='utf-8') as fe:
#     s=yaml.load(fe,Loader=yaml.FullLoader)
#     print(s)

@allure.story('断言标题')
def test_1(sh):
    assert sh == 'CRM系统-CRM软件-在线CRM试用-CRM客户管理系统-纷享销客CRM'

@allure.story('断言首页')
def test_2(ye):
    assert ye == '首页'



