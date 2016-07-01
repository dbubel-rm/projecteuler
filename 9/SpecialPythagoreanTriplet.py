"""
    Project Euler Question 9:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    Authur: thebeard@engineerbeard.com
"""
import time
def findTripletProd(abcProd):
    for i in xrange(1,abcProd):
        for j in xrange(1,abcProd):
            for k in xrange(1,abcProd):
                a,b,c  = i, j, k
                if a*a+b*b == c*c:
                    if a + b + c == abcProd:
                        return a * b * c
tStart = time.time()
print findTripletProd(1000)
print time.time() - tStart