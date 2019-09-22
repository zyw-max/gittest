#!/usr/bin/python
#-*-cod:utf-8-*-
from selenium import webdriver
from time import sleep
we = webdriver.Chrome()
we.get('https://mail.163.com/')
print(we.title)
print(we.current_url)
# sleep(2)
# we.switch_to.parent_frame()
# sleep(2)
# we.switch_to.frame('x-URS-iframe1567326380678.472')
# sleep(2)
we.find_element_by_id('switchAccountLogin').click()
sleep(2)
# we.switch_to.frame('x-URS-iframe1567326380678.472')
# sleep(2)
# we.find_element_by_xpath('//*[@id="auto-id-1567326381301"]').send_keys('zyw521521666')
# sleep(2)
we.find_element_by_id('changepage').click()



sleep(10)
we.quit()