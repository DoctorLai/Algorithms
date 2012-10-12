#!/usr/bin/env python
# http://www.zhihua-lai.com/acm

from time import *

# size of queen
n = 10

# bit hack version
ans = 0
LIM = (1 << n) - 1

def queen(row, ld, rd):
    # row: which queen
    # ld: left diag
    # rd: right diag
    global ans, LIM
    if row == LIM:
        ans += 1
        return
    pos = LIM & (~(row | ld | rd)) # valid positions
    while pos != 0:
        p = pos & (-pos)  # try rightmost one
        pos -= p;
        queen(row + p, (ld + p) << 1, (rd + p) >> 1)

start = time()
queen(0, 0, 0)
print time() - start
print ans

# recursive back tracing
ans = 0
sol = [0] * n

def chk(sol, depth):
    if depth == 0:
        return True
    for i in xrange(0, depth):
        if sol[i] == sol[depth]:
            return False
        if abs(i - depth) == abs(sol[i] - sol[depth]):
            return False
    return True;

def work(depth, row):
    global sol, ans, n
    if depth == n:
        ans += 1
        return
    for i in xrange(0, n):
        sol[depth] = i
        if chk(sol, depth):
            work(depth + 1, 0)

start = time()
work(0, 0)
print time() - start
print ans
