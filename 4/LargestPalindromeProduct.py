"""
    Project Euler Question 4:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.

    Authur: thebeard@engineerbeard.com
"""
import time
def isPalindrome(digits):
    if digits < 10:
        return True

    str_num = str(digits)
    n_digits = len(str_num)

    if n_digits % 2 != 0:
        n_digits = n_digits - 1

    for y in xrange(n_digits/2):
        if str_num[y] != str_num[len(str_num) - (y+1)]:
            return False
        elif y == (n_digits/2) - 1:
            return True


def findLargest(n):
    largestNum = 1

    for x in xrange(n):
        largestNum=largestNum*10

    largestNum = largestNum - 1
    i = largestNum
    j = largestNum
    biggestPal = 0
    scaleFactor = largestNum - (largestNum/10)

    while(i > scaleFactor):
        while(j > scaleFactor):
            if isPalindrome(i*j):
                if (i * j) > biggestPal:
                    biggestPal = i*j
            j=j-1
        j=largestNum
        i=i-1
    return biggestPal

tStart = time.time()
print findLargest(3)
print time.time() - tStart


