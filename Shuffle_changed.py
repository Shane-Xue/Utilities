"""
Shuffler
The given thing doesn’t need to be a python list;
As long as it has indexing it’s okay.
"""
import numpy

#it does not work. Therefor I deleted it.
"""def PokerShuffle(origin,times=3):
    '''
    origin is a list object
    times is the times this function will shuffle origin
    (bcs this algorithm cannot ensure randomness with one single shuffle)
    '''
    randint=numpy.random.randint
    shuffled=origin
    for a in range(times):
        shuffling=[]
        first=shuffled[:(len(shuffled)//2)]
        second=shuffled[len(shuffled)//2:]
        while first!=[] and second!=[]:
            get1=randint(1,4)
            get2=randint(1,4)
            if min(len(first),len(second))<3:
                get1=min(randint(1,4),len(first))
                get2=min(randint(1,4),len(second))
            for a in range(get1):
                '''if first==[]:
                    break
                else:'''
                shuffling.append(first.pop())
                '''try:
                    shuffling.append(first.pop())
                except IndexError as IE:
                    if str(IE).strip()=='pop from empty list':
                        break
                    else:
                        raise IE'''
            for a in range(get2):
                '''if second==[]:
                    break
                else:'''
                shuffling.append(second.pop())
                '''try:
                    shuffling.append(second.pop())
                except IndexError as IE:
                    if str(IE).strip()=='pop from empty list':
                        break
                    else:
                        raise IE'''
        if first==second:
            return shuffled
        if first==[]:
            for a in second:
                shuffling.append(a)
        elif second==[]:
            for a in first:
                shuffling.append(a)
        shuffled=shuffling
    return shuffled"""

def shuffle(listlike,start,end):
    for i in range (end-1,start,-1):
        rand=numpy.random.randint(start,i)
        listlike[i],listlike[rand]=listlike[rand],listlike[i]

def _test():
    lst=[]
    for a in range(20):
        lst.append(a)
    '''
    #test for PokerShuffle
    time1=time.time()
    PokerShuffle(lst)
    time2=time.time()
    tt=time2-time1
    print(lst)
    print('for the poker algorithm: ',tt)'''
    #test for normal Shuffle
    time3=time.time()
    shuffle(lst,0,len(lst))
    time4=time.time()
    tt2=time4-time3
    print(lst)
    print('for the normal algorithm: ',tt2)

if __name__ == '__main__':
    import time
    _test()
    del time
