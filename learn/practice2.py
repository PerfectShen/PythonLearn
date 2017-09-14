#!usr/bin/python
#-*- coding:utf-8 -*-

alist = []
widthStr = raw_input('请输入宽度:')
listWidthStr = raw_input('请输入数组的宽度:')
width = int(widthStr)
listWith = int(listWidthStr)
for x in xrange(1,listWith+1):
	alist.append(x)

print alist
print '\n\n\n\n'

subWidth = width/2
for x in xrange(0,len(alist)):
	temp = alist[x]
	pre = x - subWidth
	if pre < 0:
		pre = 0
	last = pre + width - 1
	if last > len(alist) - 1:
		pre = len(alist) - width
	tempStr = '['
	for x in xrange(0,width):
		tempnum = alist[pre + x]
		numStr = str(tempnum)
		if tempnum == temp:
			numStr = numStr + '*'
		if x == width - 1:
			tempStr = tempStr + numStr +']'
		else:
			tempStr = tempStr + numStr +','


	print tempStr


		