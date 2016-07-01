"""
    Project Euler Question 10:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.

    Authur: thebeard@engineerbeard.com
"""
import time
def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n % i == 0: return False
    return True

def sumPriimes(n):
    sum = 0
    for x in xrange(n):
        if isPrime(x): sum = sum + x
    return sum

tStart = time.time()
print sumPriimes(2000000)
print time.time() - tStart

