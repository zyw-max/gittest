#!/usr/bin/python
#-*-cod:utf-8-*-
'''
python日志模块  logging内置模块
日志得作用？
    记录代码在执行的过程中重要步骤运行时产生的信息

日志等级：由低到高
NOTSET 0  最轻微
DEBUG 10
INFO 20
WARNING 30
ERROR 40
CRITICAL 50     最严重的
'''
import logging
import coloredlogs  #第三方模块，将日志信息变成彩色输出
from datetime import datetime   #导入时间木块
logger = logging.getLogger(__name__)    # 获取当前文件名__name__
#输出日志信息到两个位置
#格式：shijian.后缀名   2019-08-06.txt
# print(datetime.now().date()) + '.txt'
#创建日志文件
log_name= str(datetime.now().date()) + '.out'
# print(log_name)
#输出到控制台
s_handler = logging.StreamHandler()
#输出到文件
f_handler=logging.FileHandler(filename=log_name,encoding='utf-8')
#设置日志输出的等级
s_handler.setLevel(logging.DEBUG)
#设置总的等级
logger.setLevel(logging.DEBUG)
#设置日志格式
'''
asctime当前时间
name 脚本的名字
levelname 日志的等级
message 日志记录的信息
'''
f_formatter=logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s %(message)s"
)
#添加日志格式
s_handler.setFormatter(fmt=f_formatter)
f_handler.setFormatter(fmt=f_formatter)

#添加日志控制器----》开关
logger.addHandler(f_handler)
logger.addHandler(s_handler)

#写一段日志
logger.info('第三级')
logger.debug('第二级')
# logger.error('第四级')
logger.critical('第六级')
logger.warning('第四级')