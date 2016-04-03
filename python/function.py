#!/usr/bin/python
# -*- coding: UTF-8 -*-

#函数

'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
'''

#定义一个函数
'''
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''



# eg 定义一自定义的函数

def printMyName() :
    "这个函数是用来打印我的名字"
    print "wangshen"
    return


printMyName()


# 按值传递参数和按引用传递参数
#所有参数（自变量）在Python里都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

def changeVars(mylist) :
    "修改一个变量"
    mylist.append([1,2,3])
    print "函数内 值" , mylist
    return


aList = [6,5]
changeVars(aList)
print "函数外 这个值" , aList


#参数

'''
以下是调用函数时可使用的正式参数类型：
必备参数
命名参数
缺省参数
不定长参数
'''


#必备参数

#命名参数
'''
命名参数和函数调用关系紧密，调用方用参数的命名确定传入的参数值。你可以跳过不传的参数或者乱序传参，因为Python解释器能够用参数名匹配参数值。用命名参数调用printme()函数：
'''
def printaVar( str , name) :
    "打印一个字符串"
    print str , name
    return


printaVar(name = "wangshen",str = "1234")  #如果是命名参数 的话  可直接指定对应的参数 传递的值  不需要 参数顺序来传递参数



# 缺省参数
'''
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。  在函数定义的时候 就直接 制定一个参数的默认值
'''


def printInfo(name , age = 20) :
    "函数说明  可以不写"
    print ("name = " ,name , "age = /n " , age)
    return

printInfo(name = "wangshen")
printInfo(name = "wangxiaoshen" , age = 24)




# 不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
'''


def printMoreVars(name , *vartuple) :
    print name
    for var in vartuple :
        print var , "\n"
    return

printMoreVars("wangshen1\n" , "sss","333")




#匿名函数

'''
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''


#lambda 函数语法

sum = lambda var1 , var2 : var1 + var2 ;

print   "相加之后的值是 \n",sum(1 , 2)


#return语句   退出当前执行的函数


#变量作用域

'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
'''


totle = 0 #声明一个全局 变量

def sumfunc(var1 , var2) :
    totle = var1 + var2   #这个totle 是 函数内声明的局部变量 - 和 外部的不是同一个
    print totle
    return

sumfunc(30 , 9)

print totle









