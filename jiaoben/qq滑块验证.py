#!/usr/bin/python
#-*-cod:utf-8-*-
from selenium import webdriver
from time import sleep
import warnings
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import selenium.webdriver.support.ui as ui      #智能等待模块

warnings.filterwarnings('ignore')
dr = webdriver.Chrome()

dr.get('https://qzone.qq.com/')
sleep(2)
print(dr.title)
# dr.switch_to.frame('login_frame')    #  切换弹框界面框架
# sleep(2)
# # dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('367832689')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('zyw2011')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')    #
# sleep(2)
# qq=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')   #切换滑动弹窗框架，
# # dr.find_element_by_xpath('')
# # sleep(2)


# drag_and_drop   拖拽：从起始位置拖到目的位置  drag_and_drop（起始，目的）
# drag_and_drop_by_offset  拖拽：从起始位置拖拽到某一个点的位置
# drag_and_drop_by_offset（起始位置，x，y）
# ActionChains(dr).drag_and_drop_by_offset(qq,180,0).perform()

# dr.get('https://qzone.qq.com/')
# sleep(2)
#
# unt = ui.WebDriverWait(dr,10)   #只能等待，等待dr元素出现，最多等待10秒，超出时间报timeout
# unt.until(lambda dr:dr.find_element_by_xpath('//*[@id="switcher_plogin"]').is_displayed())