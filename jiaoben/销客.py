#!/usr/bin/python
#-*-cod:utf-8-*-
import yaml
from appium import webdriver
from time import sleep
import pytest
#手机APP链接appium需要的信息
d={
"platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.facishare.fs",
  "appActivity": "com.fxiaoke.host.IndexActivity",
  "noReset": "true"
}
#与手机建立连接
# dr= webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(2)
# t=dr.find_element_by_id('com.facishare.fs:id/txtCenter').text
# assert t == '企信'
# print('登陆成功')
# sleep(2)
dr = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
sleep(20)
a=dr.find_element_by_id('com.facishare.fs:id/txtCenter').text
assert a == '企信'
print('登录成功')
dr.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]').click()
sleep(2)
dr.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]').click()



# t1=dr.find_element_by_id('com.facishare.fs:id/tabLayout').find_elements_by_class_name('android.widget.TextView') #com.facishare.fs:id/tabText  android.widget.TextView
# print(t1)
# for i in t1:
#     if i=='应用':
#         print(i)
#         dr.find_element_by_class_name('android.widget.TextView').click()