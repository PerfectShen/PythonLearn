#!usr/bin/python
#-*- coding:utf-8 -*-

# 计算器的实现
# 引入模块
from __future__ import division


# 加
def  add(x,y):
	 return x + y

def  sub(x,y):
	 return x - y

def  mult(x,y):
	 return x * y

def  div(x,y):
	 return x / y

# def operator(x,o,y):
# 	if o == '+':
# 		print add(x,y)
# 	elif o == '-':
# 	    print sub(x,y)
# 	elif o == '*':
# 	    print mult(x,y)
# 	elif o == '/':
# 	    print div(x,y)
# 	else:
# 		pass

# operator(1,'+',4)


# def operator(x,o,y):

operator = {'+':add,'-':sub,'*':mult,'/':div};

# print operator['/'](3,2)

def f(x,o,y):
	print operator.get(o)(x,y)

f(10,'+',4)

if __name__ == '__main__':
	print operator





