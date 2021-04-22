"""
Shuffler
The given thing doesn’t need to be a python list;
As long as it has indexing it’s okay.
"""
import numpy


def PokerShuffle(origin, times=5):
    """
    origin is a list object
    times is the times this function will shuffle origin
    (bcs this algorithm cannot ensure randomness with one single shuffle)
    """
    randint = numpy.random.randint
    shuffled = origin
    for a in range(times):
        shuffling = []
        first = shuffled[:(len(shuffled)//2)]
        second = shuffled[len(shuffled)//2:]
        while first != [] and second != []:
            get1 = randint(1, 4)
            get2 = randint(1, 4)
            for a in range(get1):
                if first == []:
                    break
                shuffling.append(first.pop())
            for a in range(get2):
                if second == []:
                    break
                shuffling.append(second.pop())
        if first == second:
            return shuffled
        if first == []:
            for a in second:
                shuffling.append(a)
        elif second == []:
            for a in first:
                shuffling.append(a)
        shuffled = shuffling
    return shuffled


def shuffle(listlike, start, end):
    listlike1 = listlike
    for i in range(end-1, start, -1):
        rand = numpy.random.randint(start, i)
        listlike1[i], listlike1[rand] = listlike1[rand], listlike1[i]


def _test():
    lst = []
    for a in range(10**5):
        lst.append(a)
    time1 = time.time()
    shuffle(lst, 0, len(lst)-1)
    time2 = time.time()
    tt = time2-time1
    print(tt)


if __name__ == '__main__':
    import time
    _test()
    del time
