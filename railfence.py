#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys


__author__ = "Ddosser"
__version__ = "v0.1"

LETTERS = "".join([chr(i) for i in xrange(32,127)])

class RailFence(object):
    """docstring for Zhalan"""
    def __init__(self):
        super(RailFence, self).__init__()
        
    def railfence_encode(self, raw_str):
        d = {}
        rows = []
        crype_text = ""

    	plain_text = "".join([s for s in raw_str.split(" ") if s])
        
        for row in xrange(2, len(plain_text)):
            if len(plain_text)%row == 0:
                rows.append(row)

        for index, sel in enumerate(rows):
            print "\033[1;32m[" + str(index) + "] " + str(sel) + " 栏\033[0m"
        try:
            inr = raw_input("请选择密码栏数[0]>")
            if inr == "":
                inr = 0
            row = rows[int(inr)]
        except:
            exit(0)

        col = len(plain_text)/row
        for c in xrange(col):
            d.update({c:plain_text[row * c : row * (c + 1)]})

        for r in xrange(row):
            for (k, v) in d.items():
                crype_text += d[k][r]
    	return crype_text

    def railfence_decode(self, en_str):
        plain = ""
        rows = []
        d = {}
        for row in range(2, len(en_str)):
            if len(en_str)%row == 0:
                rows.append(row)
            else:
                continue

        for row in rows:
            col = len(en_str)/row
            for r in range(row):
                d.update({r:en_str[r * col :col * (r+1)]})

            for c in range(col):
                for (k, v) in d.items():
                    if d[k]:
                        plain += d[k][c]
                    else:
                        continue
            plain += '\n'

        return plain

def usage():
    print '*'*60
    print "Usage: python railfence.py -[e <-k key>|d] [-f <file>] [-o <file>]"
    print "-e       escape input string or file."
    print "-d       railfence string."
    print "-f       input from file."
    print "-o       output to file."
    print "-h       for help."
    print '*'*60
    exit(0)

def main():
    args = sys.argv
    rf = RailFence()

    if len(args) < 2 or '-h' in args:
        usage()

    if '-e' in args:
        flag = False
    elif '-d' in args:
        flag = True
    else:
        usage()

    if '-f' in args:
        in_file = args[3]
        r = open(in_file, "r")
        raw_str = r.read()
        r.close()
    else:
        raw_str = raw_input("请输入：")

    if flag:
        result = rf.railfence_decode(raw_str)
    else:
        result = rf.railfence_encode(raw_str)

    if '-o' in args:
        out_file = args[5]
        w = open(out_file, "w")
        w.write(result.encode('utf-8'))
        w.close()
    else:
        print flag and "解密结果：" or "加密结果："
        print "\033[1;32m" + result + "\033[0m"
       
if __name__ == '__main__':
    main()