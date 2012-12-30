#!/usr/bin/env python
# convert.py
# http://www.zhihua-lai.com/acm
# http://rot47.net
# convert from any base

from math import floor

BASE2  = "01";
BASE8  = "01234567";
BASE10 = "0123456789";
BASE16 = "0123456789abcdef";
BASE32 = "0123456789abcdefghijklmnopqrstuvwxyz";
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
BASE75="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,!=-*(){}[]";

def convert(src, srctable, desttable):
    srclen = len(srctable)
    destlen = len(desttable)
    # first convert to base 10
    val = 0
    numlen = len(src)
    for i in xrange(numlen):
        val = val * srclen + srctable.find(src[i])
    if val < 0:
        return 0
    # then convert to any base
    r = val % destlen
    res = desttable[r];
    q = floor(val / destlen)
    while q:
        r = q % destlen
        q = floor(q / destlen)
        res = desttable[int(r)] + res;
    return res

