#!usr/bin/python
#-*- coding:utf-8 -*-
import re

s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"

s1 = re.sub(r'\[\w*\]','',s)
print s1