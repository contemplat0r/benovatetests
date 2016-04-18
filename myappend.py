# -*- coding: utf8 -*-

def myappend(a = [], num=0):
    a.append(0)
    print a


if __name__ == '__main__':
    a = [1, 2, 3]
    myappend(a)
    myappend()
    myappend()
