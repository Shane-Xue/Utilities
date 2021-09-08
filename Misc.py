"""
Very boring wheels that I sometimes use and are not in PY STL
"""

import time

def product(lst):
    """
    Returns the product of all elements of a list.
    Returns None in case of empty list.
    :params:
    :lst: A list(-like) object that is iterable, finite, 
          and has elements that can be multiplied.
    """
    if not lst:
        return None
    result = 1
    for elem in lst:
        result *= elem
    return result

def fac(n):
    return product(range(1,n+1))
    
def facComp(n):
    return n*facComp(n-1) if n!=0 else 1

def main():
    t1 = time.time()
    for a in range(900):
        fac(a)
    t2 = time.time()
    for a in range(900):
        facComp(a)
    t3 = time.time()
    return [(t2-t1),(t3-t2)]

if __name__=="__main__":
    ttot=[0,0]
    for n in range(10):
        t = main()
        ttot[0]+=t[0]
        ttot[1]+=t[1]
    print([n/10 for n in ttot])