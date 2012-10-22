#!/usr/bin/env python
# http://acm.zhihua-lai.com

from time import time

def powermod1(a, b, n):
    return a**b%n

def powermod2(a, b, n):
    r = 1
    for i in xrange(b):
        r = r * a % n
    return r
    
def powermod3(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b /= 2
        a = a * a % n
    return r

def powermod4(a, b, n):
    if b == 1:
        return a % n
    r = powermod4(a, b / 2, n)
    r = r * r % n
    if (b & 1) == 1:
        r = r * a % n
    return r

a = 2
b = 99999999
c = 147

starttime = time()
print powermod1(a, b, c)
print time() - starttime

starttime = time()
print powermod2(a, b, c)
print time() - starttime

starttime = time()
print powermod3(a, b, c)
print time() - starttime

starttime = time()
print powermod4(a, b, c)
print time() - starttime
