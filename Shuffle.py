"""
Shuffler
The given thing doesn’t need to be a python list;
As long as it has indexing it’s okay.
"""
import numpy

def PokerShuffle(origin,times=5):
    """
    origin is a list object
    times is the times this function will shuffle origin
    (bcs this algorithm cannot ensure randomness with one single shuffle)
    """
    randint=numpy.random.randint
    shuffled=origin
    for a in range(n):
        shuffling=[]
        first=[:len(shuffled)//2]
        second=[len(shuffled)//2:]
        while first!=[] and second!=[]:
            get1=randint(1,4)
            get2=randint(1,4)
            for a in range(get1):
                shuffling.append(first.pop())
            for a in range(get2):
                shuffling.append(second.pop())
        if first==[]:
            for a in second:
                shuffling.append(a)
        elif second==[]:
            for a in first:
                shuffling.append(a)
        shuffled=shuffling
    return shuffled

def shuffle(listlike,start,end):
    for i in range (start,end,-1):
        rand=numpy.random.randint(start,i)
        listlike[i],listlike[rand]=listlike[rand],listlike[i]


    