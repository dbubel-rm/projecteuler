"""
    Project Euler Question 5:
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder. What is the smallest
    positive number that is evenly divisible by all of the numbers from 1 to 20?

    Authur: thebeard@engineerbeard.com
"""
import time
def smallestMultiple(consecFactors):
    n=float(1)
    while(True):
        for (x) in xrange(1,consecFactors+1):
            if not (n / float(x)).is_integer(): break
            if x == consecFactors: return n
        n=n+1

t=time.time()
print smallestMultiple(20)
print time.time()-t