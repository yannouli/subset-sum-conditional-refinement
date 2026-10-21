"""Exact rational interval arithmetic; logarithm enclosure by a positive series.

Mathematical background: log x=2 atanh((x-1)/(x+1)). The algorithm and tail
estimate are also used in Wharton's verifier, cited in SOURCE-REVISIONS.json.
This implementation never uses floating-point values for inequality decisions.
"""
from dataclasses import dataclass
from fractions import Fraction as Q

@dataclass(frozen=True)
class Bounds:
    low: Q
    high: Q
    def __post_init__(self):
        assert self.low<=self.high
    @classmethod
    def exact(cls,value):
        return value if isinstance(value,cls) else cls(Q(value),Q(value))
    def __add__(self,value):
        b=self.exact(value);return Bounds(self.low+b.low,self.high+b.high)
    __radd__=__add__
    def __neg__(self):return Bounds(-self.high,-self.low)
    def __sub__(self,value):return self+(-self.exact(value))
    def __rsub__(self,value):return self.exact(value)+(-self)
    def __mul__(self,value):
        b=self.exact(value);v=[a*c for a in (self.low,self.high) for c in (b.low,b.high)]
        return Bounds(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,value):
        b=self.exact(value);assert b.low*b.high>0
        return self*Bounds(1/b.high,1/b.low)

def natural_log_normalized(x,terms=48):
    assert Q(1)<=x<=Q(2)
    z=(x-1)/(x+1);z2=z*z;power=z;total=Q(0)
    for j in range(terms):
        total+=2*power/(2*j+1);power*=z2
    tail=2*power/((2*terms+1)*(1-z2))
    return Bounds(total,total+tail)

LN2=natural_log_normalized(Q(2))
def binary_log(x):
    x=Q(x);assert x>0;k=0
    while x<Q(1):x*=2;k-=1
    while x>=Q(2):x/=2;k+=1
    return k+natural_log_normalized(x)/LN2

def entropy(x):
    x=Q(x);assert 0<x<1
    return -x*binary_log(x)-(1-x)*binary_log(1-x)
