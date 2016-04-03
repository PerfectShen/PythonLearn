#!/usr/bin/python
#-*- coding: UTF-8 -*-

#import sys;÷

#print "hello python 你好  世界  python";
#x = "123"
#sys.stdout.write(x + '\n')
#raw_input("\n\nPress the enter key to exit.")

#
#print '参数个数为:', len(sys.argv), '个参数。'
#print '参数列表:', str(sys.argv)




# 命令行输入参数
#
#import sys, getopt
#
#def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#       print(opts)
#       print(args)
#    except getopt.GetoptError:
#       print 'test.py -i <inputfile> -o <outputfile>'
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#          print '输入的文件为：', inputfile
#          print '输出的文件为：', outputfile
#
#if __name__ == "__main__":
#    main(sys.argv[1:])


x = 1000   #整形
y = 1000.2   #浮点型
c = "nihao"  #字符串
d = 'nihao'

print(x , y , c , d)



# 多个变量  赋值
a = b = c = 100

print(a , b , c)

x , y , z = "1" , "nihao" , 5

print(x , y , z)



#标准数据类型
'''
在内存中存储的数据可以有多种类型。
例如，person.s年龄作为一个数值存储和他或她的地址是字母数字字符存储。
Python有一些标准类型用于定义操作上，他们和为他们每个人的存储方法可能。
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''


#python 支持 复数  Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型


#Python字符串

#python的字串列表有2种取值顺序:
#从左到右索引默认0开始的，最大范围是字符串长度少1
#从右到左索引默认-1开始的，最大范围是字符串开头

#截取 字符串  （截取时候左闭右开）

s = "i love you"  #中间使用冒号
print(s[2:6]) #暑促下标2 到 6 之间的字符串  （前闭后开）

print s[2] #输出 index 是 1 的字符



print s #输出完整的字符串
print s[2:] #输出从第二个下标开始的字符串
print s * 2 #字符串输出两次
print s + "test str" # 输出连接的两个字符串



#python 列表


#定义一个列表  (截取的时候 和字符串  同理)

aList = ['abc' , 'def' , 'hig' ,'hello' , 12 , 76.0]
bList = ['nihao' , 'python']
print aList
print bList

print aList # 输出完整列表
print aList[0] # 输出列表的第一个元素
print aList[1:3] # 输出第二个至第三个的元素
print aList[2:] # 输出从第三个开始至列表末尾的所有元素
print aList * 2 # 输出列表两次
print aList + bList # 打印组合的列表



#python元组  （截取的时候 同理）

#定义一个 元组

tuple = ("a" , 133 , 'sss')
print tuple



#python 元字典
adic = {"name":"jack" , "age": 14}
print adic


#给字典 赋值
adic["sex"] = "male"
print adic


#取值的时候 何以根据下标去取值
print adic["sex"]


print adic.keys() #输出所有的键
print adic.values()  #输出所有的 值



#python 数据类型转换



#int(x [,base])               将x转换为一个整数
#long(x [,base] )             将x转换为一个长整数
#float(x)                     将x转换到一个浮点数
#complex(real [,imag])        创建一个复数
#str(x)                       将对象 x 转换为字符串
#repr(x)                      将对象 x 转换为表达式字符串
#eval(str)                    用来计算在字符串中的有效Python表达式,并返回一个对象
#tuple(s)                     将序列 s 转换为一个元组
#list(s)                      将序列 s 转换为一个列表
#set(s)                       转换为可变集合
#dict(d)                      创建一个字典。d 必须是一个序列 (key,value)元组。
#frozenset(s)                 转换为不可变集合
#chr(x)                      将一个整数转换为一个字符
#unichr(x)                   将一个整数转换为Unicode字符
#ord(x)                      将一个字符转换为它的整数值
#hex(x)                      将一个整数转换为一个十六进制字符串
#oct(x)                      将一个整数转换为一个八进制字符串





