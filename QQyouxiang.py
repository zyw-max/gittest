#!/usr/bin/python
#-*-cod:utf-8-*-
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://mail.qq.com/cgi-bin/loginpage')
print(dr.current_url)
sleep(2)
dr.switch_to.parent_frame()
dr.switch_to.frame('login_frame')
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('2393854643')
sleep(1)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('zyw2010923?')
sleep(1)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(1)
dr.find_element_by_id('composebtn').click()
sleep(1)
dr.switch_to.frame('readmailinfo_frame')
sleep(1)
dr.find_element_by_id('//*[@id="toAreaCtrl"]').send_keys('179084191@qq.com')



sleep(5)
dr.quit()
