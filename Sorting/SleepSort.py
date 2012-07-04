#!/usr/bin/env python

import threading
import time
import random

# lock array
_lk = threading.Lock()
# sorted array
_ar = []

class SleepSortThread(threading.Thread):
    """
        SleepSort Thread
        acm.zhihua-lai.com
    """

    # constructor
    def __init__(self, val):
        self.val = val
        threading.Thread.__init__(self)        

    # thread entry
    def run(self):
        global _lk, _ar
        # sleep corresponding interval
        time.sleep(self.val)
        # lock before append
        _lk.acquire()
        _ar.append(self.val)
        _lk.release()

def SleepSort(x):
    global _ar    
    ts = []
    # create threads
    for i in x:
        t = SleepSortThread(i)
        ts.append(t)

    # start threads
    for i in ts:
        i.start()

    # wait till all finished
    for i in ts:
        i.join()

    # return sorted array
    return _ar

if __name__ == "__main__":    
    x = range(1, 10)
    random.shuffle(x)
    print "before = ", x
    t1 = time.time()
    x = SleepSort(x)
    t2 = time.time() - t1
    print "after = ", x
    print "time = %.3f seconds" % t2
    
    
