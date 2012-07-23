#!/usr/bin/env python
# http://acm.zhihua-lai.com

from math import log, floor
from time import time

def chk1(n):
    if n < 1:
        return False
    if n <= 2: # 2^0 = 1, 2^1 = 2
        return True
    i = 2
    while True:
        i *= 2
        if i == n:
            return True
        if i > n:
            return False

def chk2(n):
    if n < 1:
        return False
    i = log(n, 2)
    # might have precision problem
    return abs(i - floor(i)) <= 1e-9 

def chk3(n):
    if n < 1:
        return False
    return (n & (n - 1)) == 0

def test(n, x):
    for i in xrange(0, int(n)): # launch n tests
        x(i)

if __name__ == "__main__":
    time1 = time();
    test(1e6, chk1)
    print "chk1 = %.5f" % (time() - time1)

    time1 = time();
    test(1e6, chk2)
    print "chk2 = %.5f" % (time() - time1)

    time1 = time();
    test(1e6, chk3)
    print "chk3 = %.5f" % (time() - time1)
