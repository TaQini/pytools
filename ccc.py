#!/usr/bin/python 
#coding: utf-8
#Chinese Char Counter

from sys import *
from getopt import *
from os.path import getsize as size
from jieba import *

notcc = u' \n!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
biaodian = u'，。、？！《》“”‘’～￥（）—【】'
notccplus = notcc + u'1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
filename = ""

byte = 0
chars = 0
words = 0
lines = 0
maxlen = 0

mode_B = False
mode_C = False
mode_L = False
mode_M = False
mode_CH = False
mode_W = False

# set jieba
dt.tmp_dir='./'
dt.cache_file='jieba.cache'
setLogLevel(60)

def usage():
    print ""    
    print "Chinese Char Counter"
    print ""
    print "Usage: " + argv[0] + " [cmlwLCh]" + " <filename>"
    print "-c, --bytes             print the bytes counts"
    print "-m, --chars             print the character counts"
    print "-l, --lines             print the newline counts"
    print "-w, --words             print the words counts"    
    print "-L, --max-line-length   print the length of the longest line"
    print "-C, --chinese-chars     print the chinese character counts"
    print "-h, --help              print this page"
    print ""
    print "Example: " 
    print "     ./ccc.py sample.txt"
    print "     ./ccc.py -C sample.txt"
    print "     ./ccc.py --bytes sample.txt"
    print ""
    exit(0)

def optget():
    global mode_B
    global mode_C
    global mode_L
    global mode_M
    global mode_CH
    global mode_W
    global filename    
    global byte
    
    if len(argv) < 2:
        usage()
        
    try:
        opts, args = getopt(argv[1:], "cmlwh:LC", ["bytes", "chars", "lines", "words", "help", "max-line-length", "chinese-chars"])
        filename = args[0]
        byte = size(filename)         
    except GetoptError as err:
        print str(err)
        usage()
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-c", "--bytes"):
            mode_B = True
        elif o in ("-m", "--chars"):
            mode_C = True 
        elif o in ("-l", "--lines"):
            mode_L = True
        elif o in ("-w", "--words"):
            mode_W = True
        elif o in ("-C", "--chinese-chars"):
            mode_CH = True
        elif o in ("-L", "--max-line-length"):
            mode_M = True
        else:
            assert False, "Unhandled Option"

def count():
    global chars
    global words
    global lines
    global maxlen    
 
    for line in open(filename):    
        chars += len(line.decode("utf-8"))
        if mode_W: #jieba count words
            ls = list(cut(str(line).decode("utf-8")))
            # print ls
            words += len(ls)
        
        lines += 1
        
        if mode_L: # max line length
            if len(line.decode("utf-8")) > maxlen:
                maxlen = len(line.decode("utf-8"))
    
        for c in line.decode("utf-8"):
            if mode_CH:
                if c in notccplus + biaodian:
                    chars -= 1
            elif c in notcc + biaodian:
                chars -= 1
                words -= 1

def out():
    if mode_B:
        print "bytes: " + str(byte) + "  " + filename
    elif mode_C:
        print "chars: " + str(chars) + "  " + filename
    elif mode_L:
        print "lines:" + str(lines)  + "  " + filename
    elif mode_M:
        print "max line length: " + str(maxlen)  + "  " + filename
    elif mode_W:
        print "words:" + str(words) + "  " + filename
    elif not (mode_B or mode_C or mode_L or mode_M or mode_W):
        print "chars: " + str(chars) + ', lines: ' + str(lines)  + "  " + filename    

def main():
    optget()
    try:
        count()
        print '\033[92m'
        out()
        print '\033[0m'
    except IOError:
        usage()

if __name__ == '__main__':
    main()
    
# 待完成
# 1.通过管道实现字符统计 
#   e.g. cat flag.txt | cwc.py 
#   out: chars: xx, lines: yy
# 2.可处理多个文件
#   e.g. ./ccc.py sample1.txt sample2.txt
#   out: chars: xx, lines: yy sample1.txt
#        chars: aa, lines: bb sample2.txt
# 3.支持通配符 
#   e.g. ./ccc.py -c *
#   out: 123 sample1.txt
#         34 sample2.txt
#          2 sample3.txt 