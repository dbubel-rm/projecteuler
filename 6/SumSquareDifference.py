"""
    Project Euler Question 6:
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

    Authur: thebeard@engineerbeard.com
"""
import time
def sumSquares(n):
    sumOfSquares, sumSquared = 0, 0
    for x in xrange(1, n+1):
        sumOfSquares+=x*x
        sumSquared = sumSquared + x
    return (sumSquared*sumSquared) - sumOfSquares

tStart = time.time()
print sumSquares(100)
print time.time() - tStart