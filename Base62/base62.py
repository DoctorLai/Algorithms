#!/usr/bin/env python
# http://www.zhihua-lai.com/acm
# base62 convert

from math import floor

def toBase(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def to10(num, b = 62):
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    limit = len(num)
    res = 0
    for i in xrange(limit):
        res = b * res + base.find(num[i])
    return res

if __name__ == "__main__":
    for x in xrange(100000):
        y = toBase(x)
        z = to10(y)
        if x != z:
            print "error, " + x
    print "end"
