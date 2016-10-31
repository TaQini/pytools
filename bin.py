#!/usr/bin/python 
#coding: utf-8
import sys
from getopt import *

flag = 0
mode_G = 0
mode_I = 0

class fc:
    BLUE = '\033[34m'
    RED = '\033[91m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'
    ERROR = '\033[093m'
def usage():
    print 
    print "Transform decimal integer to binary string"
    print 
    print "Usage: " + sys.argv[0] + " [gih] <integer>" 
    print "-g, --graph         print the graph of decimal integer"
    print "-i, --interactive   use interactive mode"
    print "-i, --help          print this page"
    print     
    print "Example: "
    print "     ./bin.py 9"
    print "     ./bin.py -g 9"
    print "     ./bin.py -gi"
    print 
    exit(0)
    
def graph(s):
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    s5 = ""
    s6 = ""
    for c in s:
        if c == "1":
            s1 += "***@***"
            s2 += "*@@@***"
            s3 += "***@***"
            s4 += "***@***"
            s5 += "***@***"
            s6 += "*@@@@@*"            
        if c == "0":
            s1 += "*@@@@@*"
            s2 += "*@***@*"
            s3 += "*@***@*"
            s4 += "*@***@*"
            s5 += "*@***@*"
            s6 += "*@@@@@*"
    print s1
    print s2
    print s3
    print s4
    print s5
    print s6
    if not mode_I:
        print         
        exit(0)

def interactive():
    i = 1
    while True:
        try:
            a = raw_input(fc.BLUE + "In [" + str(i) + "]: " + fc.ENDC)    
            s = bin(int(a))[2:]
        except KeyboardInterrupt:
            print             
            print "KeyboardInterrupt"           
            print fc.GREEN + " --Thanks for using bin" + fc.ENDC   
            print 
            exit(0)
        except ValueError:
            print fc.ERROR + "[!] " + fc.ENDC + "ValueError: ",
            print "Please input a decimal integer."
            i += 1 
            print
        else:
            if mode_G:
                print fc.RED + "Out[" + str(i) + "]: " + fc.ENDC
                graph(s)
                print 
            else:
                print fc.RED + "Out[" + str(i) + "]: " + fc.ENDC + s + "\n"
            i += 1            
def main():
    global flag
    global mode_G
    global mode_I
    
    try:
        opts, args = getopt(sys.argv[1:], "gih" ,["graph","interactive","help"])
    except GetoptError as err:
        print str(err)
        usage()        
    
    if len(sys.argv) < 2:
        usage()   
    
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        if o in ("-g", "--graph"):
            mode_G = 1
        if o in ("-i", "interactive"):
            mode_I = 1             
    try:
        s = bin(int(args[-1]))[2:]
    except ValueError:        
        print fc.ERROR + "[!] " + fc.ENDC + "ValueError: ",
        print "Please input a decimal integer."                       
        usage()
    except IndexError:
        pass
    if mode_G and not mode_I:            
        graph(s) 
    elif mode_I:
        interactive()
    else:
        print s
        print 

if __name__ == '__main__':
    main()
