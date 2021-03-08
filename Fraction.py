"""
A fraction class to enhance ability of python calculations.
The idea comes from the Haskell Language.
"""

from numpy import sign
import math

def GCF(a,b):
    a=math.abs(a)
    b=math.abs(b)
    while b>0:
        a,b=b,a%b
    return a

class fraction():
    def __init__(self,divided,divider=1):
        """
        Representation in the form of divided/divider
        We make sure the result has its negative sign (if present) on the divided
        And that the fraction has been simplified.
        """
        if type(divided)==fraction:
            self=divided
        elif divider==0:
            raise ZeroDivisionError("The divider of a fraction cannot be zero!")
        sd=math.sign(divided)
        sr=math.sign(divider)
        sf=sr*sd
        divided=abs(divided/GCF(divided,divider))
        divider=abs(divider/GCF(divided,divider))
        self.divided=sf*divided
        self.divider=divider
    def __add__(self,other):
        """
        Add two fractions
        """
        other=fraction(other)
        return fraction(self.divided*other.divider,other.divided*self.divider,self.divider*other.divider)
    def __pos__(self):
        return self
    def __neg__(self):
        return fraction(-self.divided,self.divider)
    def __sub__(self,other):
        """
        Subtract two fractions
        """
        other=fraction(other)
        return self+(-other)
    def __abs__(self):
        return fraction(abs(divided),divider)
    def __mul__(self,other):
        other=fraction(other)
        return fraction(self.divided*other.divided,self.divider*other.divider)
    def __div__(self,other):
        other=fraction(other).reciprocal()
        return self*other
    def __floor__(self):
        return self.divided%self.divider
    def __ceil__(self):
        return math.floor(self)+1
    def __eq__(self,other):
        return self.divided==other.divided and self.divider==other.divider
    def __ne__(self,other):
        return not self==other
    def __lt__(self,other):
        if self.sign()<other.sign():
            return True
        elif self.sign()*other.sign()!=1:
            return False
        #unfinished
    def reciprocal(self):
        return fraction(self.divider,self.divided)
    def sign(self):
        return sign(self.divided)
