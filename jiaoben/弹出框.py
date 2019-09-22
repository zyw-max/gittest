#!/usr/bin/python
#-*-cod:utf-8-*-
from selenium import webdriver
from time import sleep
import warnings

warnings.filterwarnings('ignore')
dr = webdriver.Chrome()
# dr.get('file:///D:/QQchuanshu/abc.html')
# sleep(3)
# dr.find_element_by_xpath('/html/body/button').click()
# sleep(2)
# #切换到弹出框
# ww=dr.switch_to_alert()
# #获取弹出框上的文本
# print(ww.text)
# sleep(2)
# #输入数据
# ww.send_keys('python')
# sleep(2)
# #点击弹出框上面的确定
# ww.accept()
# #点击取消
# # ww.dismiss()
#
#
# sleep(2)
# dr.quit()




# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3fc977e4034f487da0384250b4138c12')
# #JavaScript中对应的滚动条:arguments[0].scrollIntoView();
# #滚动到指定位置
# sleep(2)
# dd = dr.find_element_by_xpath('//*[@id="J_footer"]/div[2]/div/div/div[1]/h5')    #定位到的滚动位置
# #execute执行JavaScript语句，dd是要滚动到的位置
# sleep(2)
# dr.execute_script('arguments[0].scrollIntoView();',dd)

#按照距离滚动，一次滚动200，总距离10000
# for i in range(0,10000,200):
#     js=f"var q=document.documentElement.scrollTop={i}"
#     dr.execute_script(js)
#     sleep(2)




from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep


dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3fc977e4034f487da0384250b4138c12')
sleep(3)
# dd=dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[16]/a[3]')
#
#
# #将鼠标移动到元素中心
# #动作连
# ActionChains(dr).move_to_element(dd).perform()
'''错误

# aa=dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[5]')
# sleep(2)
# for i in aa:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(1)
'''

jd =dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
sleep(1)
for i in jd:
    ActionChains(dr).move_to_element(i).perform()

sleep(5)
dr.quit()