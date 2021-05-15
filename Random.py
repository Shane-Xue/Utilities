"""
random number generator wrapper class
"""
import math
import numpy as np
from random import random

SmallToBig = lambda a,b : (a,b) if a < b else (b,a)


class RandGen():
    def __init__(self, ceil, floor=0, randness=3):
        floor, ceil = SmallToBig(floor, ceil)
        self.range = ceil-floor+1
        self.floor = floor
        #make sure the magnitude of randomness is
        #AT LEAST 3 magnitudes bigger than the range
        if randness > math.log(self.range,10) + 3:
            self.randness = randness
        else:
            self.randness = math.log(self.range,10) + 3
    
    def gen(self):
        return (math.ceil(random() * ((10 ** self.randness) * self.range + 1) % self.range) + self.floor)

    def __call__(self):
        return self.gen()

def _TestGen(floor,ceil,randness=3,tests=10**5):
    SmallToBig(floor,ceil)
    rg=RandGen(ceil,floor,randness)
    lst=list()
    for a in range(floor,ceil+1):
        lst.append(0)
    for a in range(tests):
        lst[rg.gen()-floor]+=1
    return lst

def _TestGenNp(floor,ceil,tests=10**5):
    lst=[]
    for a in range(floor,ceil+1):
        lst.append(0)
    for a in range(tests):
        lst[np.random.randint(floor,ceil)-floor]+=1
    return lst

def _CompTime(floor,ceil,tests=10**6):
    t1=time.time()
    gen=RandGen(floor,ceil-1)
    for a in range(tests):
        gen()
    t2=time.time()
    t3=time.time()
    for a in range(tests):
        np.random.randint(floor,ceil)
    t4=time.time()
    tt1=t2 - t1
    tt2=t4 - t3
    print('numpy time:',tt2)
    print('wheel time:',tt1)

if __name__ == '__main__':
    import time
    _CompTime(1,1000)

#testing data:
#1~4, 10**5 tests:
#   numpy 0.5s
#   wheel 0.15s
#   diff 0.35s
#1~1000, 10**6 tests:
#   numpy 5.4s
#   wheel 1.5s
#   diff 3.9s