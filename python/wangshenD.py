#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import sys;÷

#print "hello python 你好  世界  python";
#x = "123"
#sys.stdout.write(x + '\n')
#raw_input("\n\nPress the enter key to exit.")

#
#print '参数个数为:', len(sys.argv), '个参数。'
#print '参数列表:', str(sys.argv)




# 命令行输入参数

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
       print(opts)
       print(args)
    except getopt.GetoptError:
       print 'test.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print 'test.py -i <inputfile> -o <outputfile>'
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
          print '输入的文件为：', inputfile
          print '输出的文件为：', outputfile

if __name__ == "__main__":
    main(sys.argv[1:])