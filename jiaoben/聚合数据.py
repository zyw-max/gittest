#!/usr/bin/python
#-*-cod:utf-8-*-
import json, urllib
# from urllib.request import urlencode
import urllib.request
from urllib.parse import urlencode


def main():
    # 配置您申请的APPKey
    appkey = "3b160650fc930fd456bd565649dbf778"

    # 1.菜谱大全
    request1(appkey, "GET")

    # 2.分类标签列表
    request2(appkey, "GET")

    # 3.按标签检索菜谱
    request3(appkey, "GET")

    # 4.按菜谱ID查看详细
    request4(appkey, "GET")


# 菜谱大全
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/cook/query.php"
    params = {
        "menu": "",  # 需要查询的菜谱名
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json
        "pn": "",  # 数据返回起始下标
        "rn": "",  # 数据返回条数，最大30
        "albums": "",  # albums字段类型，1字符串，默认数组

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 分类标签列表
def request2(appkey, m="GET"):
    url = "http://apis.juhe.cn/cook/category"
    params = {
        "parentid": "",  # 分类ID，默认全部
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 按标签检索菜谱
def request3(appkey, m="GET"):
    url = "http://apis.juhe.cn/cook/index"
    params = {
        "cid": "",  # 标签ID
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json
        "pn": "",  # 数据返回起始下标，默认0
        "rn": "",  # 数据返回条数，最大30，默认10
        "format": "",  # steps字段屏蔽，默认显示，format=1时屏蔽

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 按菜谱ID查看详细
def request4(appkey, m="GET"):
    url = "http://apis.juhe.cn/cook/queryid"
    params = {
        "id": "",  # 菜谱的ID
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


if __name__ == '__main__':
    main()