#!/usr/bin/python
#-*-cod:utf-8-*-
# 接口测试：验证URL是否能正常请求和响应的过程
import requests
import json
class Zuowen():
    url = "http://v.juhe.cn/weather/index"

    # querystring = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "%E5%8C%97%E4%BA%AC"}
    headers = {
        'Content-Type': "text/plain",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "650980a8-3176-4be9-9258-eddcd32e196b,f3d2d7e3-e0e2-46c7-b351-f81c7f663a34",
        'Host': "v.juhe.cn",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    def test_1(self):
        # querystring = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "%E5%8C%97%E4%BA%AC"}
        par= {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "周口"}
        res=requests.get(url=self.url,headers=self.headers,params=par)
        res.content.decode('utf-8')
        html = res.json()   # 讲json字符串转化成字典
        print(html)
        assert html['resultcode'] == "200"
        # html = json.loads(html)   # 讲json字符串转化成字典

    # print(response.text)
    def test_2(self):
        par = {"key": "e78cd733cf6a1cb9de1ca62f5c869b3c", "cityname": "郑州"}
        res = requests.get(url=self.url, headers=self.headers, params=par)
        html = res.json()
        # print(html)
        assert html['reason'] == "successed!"



tt = Zuowen()
tt.test_1()
tt.test_2()