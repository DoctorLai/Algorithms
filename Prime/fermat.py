#!/usr/bin/env python

from random import *

seed()

def powmod(a, b, n):
    if b == 1:
        return a % n
    r = powmod(a, b / 2, n)
    r = r * r % n
    if (b & 1) == 1: # odd number
        r = r * a % n
    return r

def probalPrime(n, s):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in xrange(s):
        a = randint(2, n - 1)
        if powmod(a, n - 1, n) != 1:
            return False
    return True

for _ in xrange(1, 100):
    if probalPrime(_, 10):
        print _

