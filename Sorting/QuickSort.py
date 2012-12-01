#!/usr/bin/env python
"""
 
http://acm.zhihua-lai.com
 
    QuickSort.py
    Quick Sorting Algorithm
    01/Dec/2012
"""
 
from random import *
from time import *
 
seed()
x = []
for i in range(0, 10):
    x.append(randint(0, 100))
 
def qsort(x, l, r):
    i = l
    j = r
    p = x[l + (r - l) / 2] # pivot element in the middle
    while i <= j:
        while x[i] < p: i += 1
        while x[j] > p: j -= 1
        if i <= j: # swap 
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    if l < j: # sort left list
        qsort(x, l, j)
    if i < r: # sort right list
        qsort(x, i, r)
    return x

start = time()
print "Before: ", x
x = qsort(x, 0, len(x) - 1)
print "After: ", x
print "%.2f seconds" % (time() - start)
