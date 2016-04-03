#!/usr/bin/python
#-*- coding: UTF-8 -*-



#时间 和 日期


import time;  # 引入系统的时间  库
import calendar;  #引入日历库


timeintival = time.time()

print timeintival #打印当前时间 到  1970年的 时间戳  单位 秒



#时间元组

'''
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''

'''
序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''


#获取当前时间

localtime = time.localtime(time.time()) #获取到当前的时间 元组合
print localtime

#获取格式化成字符串的时间
localtimeStr = time.asctime(time.localtime(time.time()))  #获取到时间戳 然后 转换成 时间元组 再格式化成字符串
print localtimeStr


#获取某月日历

cal  = calendar.month(2008,1);
print "2008 年  一月的 日历 \n"

print cal


#time 内置 函数


# 扩展

#其他 和时间哦日期相关的  库
'''
datetime模块
pytz模块
dateutil模块
'''


