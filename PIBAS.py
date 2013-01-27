#!/usr/bin/env python

class PIBAS:
    """
        PIBAS Interpreter
        http://acm.timus.ru/problem.aspx?space=1&num=1230
        http://www.zhihua-lai.com/acm
    """

    """
        private attribute to store string vars
    """
    __vars__ = []

    """
        constructor
    """
    def __init__(self):
        # 26 upper-case string vars possible
        self.__vars__ = [''] * 26

    """
        throw an error when parsing source string
    """
    def __err(self, src, msg, pos):
        raise Exception(src + ": Pos: " + str(pos) + ": " + msg)        

    """
        parse a string result
        e.g. A+B
        e.g. 'test'+'abc'+$(A,1,2)+B
    """
    def __gets__(self, src):
        tmp = ''
        k = len(src)
        i = 0
        s = 0
        d = 0
        last = 0
        sgn = 1
        while i < k:
            c = src[i]
            if c == '"' and s == 0:
                if d == 0:
                    d = 1
                    last = i + 1
                elif sgn == 1:
                    tmp += src[last:i]
                    sgn = 0
                    d = 0
                elif sgn == 0:
                    self.__err(src, "Missing +", i)
                else:
                    self.__err(src, "Extra +", i)
            elif c == "'" and d == 0:
                if s == 0:
                    s = 1
                    last = i + 1
                elif sgn == 1:
                    tmp += src[last:i]
                    sgn = 0
                    s = 0
                elif sgn == 0:
                    self.__err(src, "Missing +", i)
                else:
                    self.__err(src, "Extra +", i)
            elif c == '$' and s == 0 and d == 0:
                if sgn == 1:
                    if i + 7 >= k:
                        self.__err(src, "Invalid $ pattern", i)
                    elif src[i + 1] != '(':
                        self.__err(src, "Missing (", i)
                    else:
                        i += 2
                        j = i
                        tt = -1
                        while j < k:
                            if src[j] == ')':
                                tt = j
                                break                            
                            j += 1
                        if tt == -1:
                            self.__err(src, "Missing )", i)
                        else:
                            xx = src[i:tt]
                            yy = xx.split(",")
                            if len(yy) == 3:
                                if len(yy[0]) == 1 and yy[0] >= 'A' and yy[0] <= 'Z':
                                    sgn = 0
                                    idx = int(yy[1]) - 1
                                    lll = int(yy[2])
                                    tmp += self.__vars__[ord(yy[0]) - 65][idx:idx+lll]
                                    i = tt
                                else:
                                    self.__err(src, "Invalid string var " + yy[0], i)
                            else:
                                self.__err(src, "Invalid $, require 3 parts: ", i)
                elif sgn == 0:
                    self.__err(src, "Missing +", i)
                else:
                    self.__err(src, "Extra +", i)                
            elif c == '+' and s == 0 and d == 0:
                if sgn > 0:
                    self.__err(src, "Too many string +", i)
                else:
                    sgn = 1
            elif c >= 'A' and c <= 'Z' and s == 0 and d == 0:
                if sgn == 1:
                    tmp += self.__vars__[ord(c) - 65]
                    sgn = 0
                elif sgn == 0:
                    self.__err(src, "Missing +", i)
                else:
                    self.__err(src, "Extra +", i)
            elif s == 0 and d == 0:
                self.__err(src, "Invalid Char: " + c, i)
            i += 1
        return tmp

    """
        parse each single statement; string assignment or print
    """
    def __parse(self, src):
        k = len(src)
        i = 0
        s = ""
        while i < k:
            c = src[i]
            if c >= 'A' and c <= 'Z':
                if i + 1 < k and src[i + 1] == '=':
                    self.__vars__[ord(c) - 65] = self.__gets__(src[i + 2:])
                    break
                else:
                    self.__err(src, "Missing assignment", i)
            elif c == '?':
                s += self.__gets__(src[i + 1:])
                break
            else:
                self.__err(src, "Invalid Char " + c, i)
            i += 1
        return s

    """
        main entry to interpreting PIBAS
    """
    def Parse(self, src):
        """
            split the statements
        """
        k = len(src)
        i = 0
        s = 0
        d = 0
        last = 0
        out = ""
        while i < k:
            c = src[i]
            if c == ';':
                if s == 0 and d == 0:
                    out += self.__parse(src[last:i])
                    last = i + 1
            elif c == '"' and s == 0:
                if d == 1:
                    d = 0
                else:
                    d = 1
            elif c == "'" and d == 0:
                if s == 1:
                    s = 0
                else:
                    s = 1
            i += 1
        if last != k:
            if s == 0 and d == 0:
                out += self.__parse(src[last:])
            else:
                self.__err(src, "Unclosed string constant", k - 1)
        print out

if __name__ == "__main__":
    obj = PIBAS();
    src = """A='World, Hello!';?$(A,8,5);?", ";B=$(A,1,5)+'!';?B"""
    print "PIBAS Source: "
    print src
    print "PIBAS Output: "
    obj.Parse(src);
