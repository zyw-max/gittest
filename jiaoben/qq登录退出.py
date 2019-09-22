#!/usr/bin/python
#-*-cod:utf-8-*-
import yaml
from appium import webdriver
from time import sleep
with open(file=r"E:\ruanjianceshi\QQ项目\element\e.yaml",mode='r',encoding='utf-8') as fb:
      s = yaml.load(fb,Loader=yaml.FullLoader)
      # print(s)
# 手机app链接appium是所需要的信息
d = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.tencent.mobileqq",
      "appActivity": ".activity.SplashActivity",
      "noReset": "true"
}

# 与手机建立连接
dr = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
#导入休眠，等待app完全启动
sleep(5)
# 实现登陆
# 第一步：点击登录按钮
dr.find_element_by_id(s['l'][0]).click()
sleep(1)
# 第二步：向账号的输入框输入自己的账号
dr.find_element_by_id(s['k'][0]).find_element_by_class_name(s['k'][1]).click()  #点击账号输入框
sleep(1)
dr.find_element_by_id(s['k'][0]).find_element_by_class_name(s['k'][1]).send_keys(['2393854643'])  #输入账号
#第三步想密码输入框输入密码
dr.find_element_by_id(s['k'][2]).send_keys('zyw2010923?')
#第四步点击登录按钮
dr.find_element_by_id(s['k'][3]).click()      #点击登录按钮
sleep(3)
# t = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.TextView')
# for i in t:
#     print(i.text)

dr.find_element_by_id('com.tencent.mobileqq:id/conversation_head').click()   #登录成功点击头像区域
sleep(2)
dr.find_element_by_id('com.tencent.mobileqq:id/settings').click()   #点击个人资料左下角的设置区域
sleep(2)
dr.find_element_by_id('com.tencent.mobileqq:id/account_switch').click()  #点击账号管理区域
sleep(2)
dr.find_element_by_id('com.tencent.mobileqq:id/logoutBtn').click()    #点击退出当前qq
sleep(1)
dr.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()    #点击确认退出
sleep(2)
dr.find_element_by_xpath('//android.widget.ImageView[@content-desc="帐号列表"]').click()
sleep(2)
dr.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()