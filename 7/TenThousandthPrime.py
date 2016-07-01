"""
    Project Euler Question 7:
    By listing the first six prime numbers: 2, 3, 5, 7, 11,
    and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?

    Authur: thebeard@engineerbeard.com
"""
import time

def isPrime2(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n % i == 0:
            return False

    return True

def findNthPtime(n):
    primeCount = 0
    i = 0
    while(primeCount < n):
        if isPrime2(i):
            primeCount+=1
        i+=1
    return i-1

tStart = time.time()
print findNthPtime(10001)
print time.time - tStart