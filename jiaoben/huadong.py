#!/usr/bin/python
#-*-cod:utf-8-*-

import yaml
from appium import webdriver
from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as es
from selenium.webdriver.common.by import By
d={
"platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity",
  "noReset": "true"
}
#与手机建立连接
dr= webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=d)    #desired_capabilities=d
sleep(10)
s=dr.get_window_size()    #获取手机屏幕或模拟器尺寸
print(s)
#第二步手机的比例尺寸
x1=s['width']*0.1
print(x1)
x2=s['width']*0.78
print(x2)
y1=s['height']*0.2
print(y1)
y2=s['height']*0.75
print(y2)
def shang():
    dr.swipe(x1,y1,x1,y2)
    sleep(5)
def xia():
    dr.swipe(x1,y2,x1,y1)
def zuo():
    dr.swipe(x2,y1,x1,y1)
    sleep(5)
def you():
    dr.swipe(x1,y1,x2,y1)
    sleep(5)

# xia()
# sleep(10)
# shang()
# sleep(10)
you()
sleep(10)
print('右滑完成')
zuo()
sleep(10)
print('左滑完成')
# while True:
#     xia()
#     sleep(25)


# WebDriverWait(driver=dr, timeout=10, poll_frequency=0.5).until(EC.presence_of_element_located())    #EC.presence_of_element_located(元素，必须写成一个元组)  等待某个元素出现
#元素（BY.id,元素)
# d=dr.get_screenshot_as_base64()   #二进制截图
# f=dr.get_screenshot_as_file()     #保存图片到指定文件中
# g=dr.get_screenshot_as_png()        #