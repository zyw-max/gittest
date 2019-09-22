#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://qzone.qq.com')
print(dr.title)
print(dr.current_url)
sleep(2)
dr.switch_to.parent_frame()
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('2393854643')
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('zyw2010923?')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()