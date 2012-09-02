#!/usr/bin/env python
# http://www.zhihua-lai.com/acm

def extended_gcd1(a, b):
    x = 0
    y = 1
    lastx = 1
    lasty = 0
    while b != 0:
        quo = a / b
        a, b = b, a % b
        x, lastx = lastx - quo * x, x
        y, lasty = lasty - quo * y, y
    return (lastx, lasty)


def extended_gcd2(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = a / b, a % b
        s, t = extended_gcd2(b, r)
        return (t, s - q * t)

def extended_gcd3(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        q, r = a / b, a % b
        u, s, t = extended_gcd3(b, r)
        return (u, t, s - q * t)
    
if __name__ == "__main__":
    print extended_gcd1(27, 21)
    print extended_gcd2(27, 21)
    print extended_gcd3(27, 21)
    
