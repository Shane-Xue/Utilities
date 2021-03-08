”””
A fraction class to enhance ability of python calculations.
The idea comes from the Haskell Language.
”””
import math

def GCF(a,b):
    a=math.abs(a)
    b=math.abs(b)
    

class fraction():
    def __init__(self,divided,divider):
        ”””
        Representation in the form of divided/divider
        We make sure the result has its negative sign (if present) on the divided
        And that the fraction has been simplified.
        ”””
        sd=math.sign(divided)
        sr=math.sign(divider)
        sf=sr*sd
        divided=divided/GCF(divided,divider)
        divider=divider/GCF(divided,divider)
        self.divided=sf*divided
        self.divider=divider
    def __add__(self,other):
        ”””
        Add two fractions
        ”””
        return fraction(self.divided*other.divider+other.divided*self.divider,self.divider*other.divider)
    def __pos__(self):
        return self
    def __neg__(self):
        return fraction(-self.divided,self.divider)
    def __sub__(self,other):
        ”””
        Subtract two fractions
        ”””
        return self+(-other)