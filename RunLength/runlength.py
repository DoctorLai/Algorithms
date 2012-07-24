#!/usr/bin/env python
# http://acm.zhihua-lai.com

def runlen(s):
    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i - 1]:# check if is the same letter
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt) # store the previous data
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r

if __name__ == "__main__":
    print runlen("aaabbccccddddd")
    print runlen("a")
    print runlen("")
    print runlen("abcdefg")
    print runlen("eeeeeaaaff")
