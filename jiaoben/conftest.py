#!/usr/bin/python
#-*-cod:utf-8-*-
import pytest
import requests
from fenxiang.until.duqu import Cheng as d
# import sys,os
# sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
#写配置代码../
from selenium import webdriver
import pytest
import allure
import yaml

dr=webdriver.Chrome()
dr.get('https://www.fxiaoke.com/?utm_source=%E7%99%BE%E5%BA%A6&utm_medium=SEM&utm_term=%E6%A0%87%E9%A2%98&utm_content=%E5%B7%A6%E4%BE%A7&utm_campaign=%E5%93%81%E4%B8%93&e_keywordid={keywordid}&e_keywordid2=111642263163')
with open(file=r'E:\ruanjianceshi\纷享销客\element\fen.yaml',mode='r',encoding='utf-8') as fe:
    s=yaml.load(fe,Loader=yaml.FullLoader)
@pytest.fixture(params=d())
def sh():

    b=dr.title
    return b
@pytest.fixture(params=d())
def ye():
    e=dr.find_element_by_xpath(s['f'][0]).text
    return e

# @pytest.fixture(params=d())
# def tianqi_1(request):
#     url = "http://v.juhe.cn/weather/index"
#     headers = {
#         'Content-Type': "text/plain",
#         'User-Agent': "PostmanRuntime/7.17.1",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "650980a8-3176-4be9-9258-eddcd32e196b,f3d2d7e3-e0e2-46c7-b351-f81c7f663a34",
#         'Host': "v.juhe.cn",
#         'Accept-Encoding': "gzip, deflate",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#     }
#     par = {"key":"e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname":f"{request.param}"}
#     res = requests.get(url=url, headers=headers, params=par)
#     return res.json()
# # @pytest.fixture()
# def tianqi_2():
#     url = "http://v.juhe.cn/weather/uni"
#
#     querystring = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c"}
#
#     headers = {
#         'User-Agent': "PostmanRuntime/7.17.1",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "65f518d1-6f1b-4d18-831f-bc4063c98aec,d424ec2e-87e4-45e2-ba10-4cd2d012db36",
#         'Host': "v.juhe.cn",
#         'Accept-Encoding': "gzip, deflate",
#         'Cookie': "aliyungf_tc=AQAAAGyspXaVrQMA1DR4toCjgQCG7JMX",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     return response.json()
#
#
#     print(response.text)
#
# tianqi_2()





# class Zuowen():
#     url = "http://v.juhe.cn/weather/index"
#
#     # querystring = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "%E5%8C%97%E4%BA%AC"}
#     headers = {
#         'Content-Type': "text/plain",
#         'User-Agent': "PostmanRuntime/7.17.1",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "650980a8-3176-4be9-9258-eddcd32e196b,f3d2d7e3-e0e2-46c7-b351-f81c7f663a34",
#         'Host': "v.juhe.cn",
#         'Accept-Encoding': "gzip, deflate",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#     }
#
#     # response = requests.request("GET", url, headers=headers, params=querystring)
#     def test_1(self):
#         # querystring = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "%E5%8C%97%E4%BA%AC"}
#         par= {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "周口"}
#         res=requests.get(url=self.url,headers=self.headers,params=par)
#         res.content.decode('utf-8')
#         html = res.json()   # 讲json字符串转化成字典
#         # print(html)
#         assert html['resultcode'] == "200"
#         return
#         # html = json.loads(html)   # 讲json字符串转化成字典
#
#     # print(response.text)
#     def test_2(self):
#         par = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "郑州"}
#         res = requests.get(url=self.url, headers=self.headers, params=par)
#         html = res.json()
#         # print(html)
#         assert html['reason'] == "successed!"
#
#
#
# tt = Zuowen()
# tt.test_1()
# tt.test_2()