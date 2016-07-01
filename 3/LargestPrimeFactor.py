"""
    Project Euler Question 3:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    Authur: thebeard@engineerbeard.com
"""
import math
import time

def fermatFactorization(n):
    a = math.ceil(math.sqrt(n))
    b2 = (a*a) - n
    while not math.sqrt(b2).is_integer():
        a+=1
        b2 = (a*a) - n
    b=math.sqrt(b2)
    return [(a-b), (a+b)]

def findPrimeFactors(factorList):
    primeFactors = []
    for n in factorList:
        [primeFactors.append(t) for t in fermatFactorization(n)]
    print "List of prime factors:", primeFactors
    return max(primeFactors)

def findLargestPrimeFactor(n):
    return findPrimeFactors(fermatFactorization(n))


tStart = time.time()
print findLargestPrimeFactor(600851475143)
print time.time() - tStart, "seconds elapsed"




