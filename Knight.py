#!/usr/bin/env python

class Knight:
    """
        Knight Tour
        http://www.zhihua-lai.com/acm
    """

    """
        private attributes
    """
    __sizex  = 8
    __sizey  = 8
    __startx = 1
    __starty = 1
    __endx   = __sizex
    __endy   = __sizey

    """
        get properties wrappers
    """
    def __getsizex(self):
        return self.__sizex

    def __getsizey(self):
        return self.__sizey

    def __getsx(self):
        return self.__startx

    def __getsy(self):
        return self.__starty

    def __getendx(self):
        return self.__endx

    def __getendy(self):
        return self.__endy
    
    """
        set properties wrappers
    """
    def __setsizex(self, v):
        self.__sizex = v

    def __setsizey(self, v):
        self.__sizey = v

    def __setsx(self, v):
        self.__startx = v

    def __setsy(self, v):
        self.__starty = v

    def __setendx(self, v):
        self.__endx = v

    def __setendy(self, v):
        self.__endy = v

    """
        properties
    """
    StartX = property(__getsx, __setsx)
    StartY = property(__getsy, __setsy)
    EndX   = property(__getendx, __setendx)
    EndY   = property(__getendy, __setendy)
    SizeX  = property(__getsizex, __setsizex)
    SizeY  = property(__getsizey, __setsizey)
    
    """
        constructor
    """
    def __init__(self, start, end):
        x1 = ord(start[0]) - 64
        y1 = 9 - int(start[1])
        x2 = ord(end[0]) - 64
        y2 = 9 - int(end[1])
        self.StartX = x1
        self.StartY = y1
        self.EndX   = x2
        self.EndY   = y2

    """
        check if (x, y) is a valid position
    """
    def Check(self, x, y):
        if x <= 0 or x > self.SizeX:
            return False
        if y <= 0 or y > self.SizeY:
            return False
        return True

    """
        convert (x, y) to string representation
        e.g. (1, 1) to a1
    """
    @staticmethod
    def ConvertPosition(x, y):        
        return chr(64 + x) + str(9 - y)
    
    """
        print the moves
    """
    @staticmethod
    def Print(moves):
        for xy in moves:
            print Knight.ConvertPosition(xy[0], xy[1]),

    def Solve(self):
        if self.SizeX <= 0:
            raise Exception("SizeX <= 0")
        if self.SizeY <= 0:
            raise Exception("SizeY <= 0")
        if not self.Check(self.StartX, self.StartY):
            raise Exception("Start Position Invalid")
        if not self.Check(self.EndX, self.EndY):
            raise Exception("End Position Invalid")
        # offsets for next knight positions
        offset = [(1, 2), (-1, -2), (1, -2), (-1, 2),
                  (2, 1), (-2, -1), (2, -1), (-2, 1)]
        q = []
        # add init position
        q.append((self.StartX, self.StartY, []))
        history = [(self.StartX, self.StartY)]
        while len(q):
            # pop from the queue
            cur = q.pop(0)
            if cur[0] == self.EndX and cur[1] == self.EndY:
                Knight.Print(cur[2])
                break
            for xy in offset:
                curx = xy[0] + cur[0]
                cury = xy[1] + cur[1]
                if self.Check(curx, cury) and (not (curx, cury) in history):
                    history.append((curx, cury))
                    curmove = [_ for _ in cur[2]]
                    curmove.append((curx, cury))
                    q.append((curx, cury, curmove))

if __name__ == "__main__":
    obj = Knight("A8", "B7")
    obj.Solve()
