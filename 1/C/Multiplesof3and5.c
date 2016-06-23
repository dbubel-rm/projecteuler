/*
	Project Euler Question 1:
	If we list all the natural numbers below 10 that are multiples of 3 or 5, 
	we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of 
	all the multiples of 3 or 5 below 1000.

	Author: thebeard@engineerbeard.com
*/
#include <stdio.h>
#include <stdint.h>

int main()
{
    int factorSum = 0;
    for(int i = 1; i < 1000; i++)
    {
        if(i % 3 == 0 || i % 5 == 0)
        {
            factorSum = factorSum + i;
        }
    }
    printf("%i\n", factorSum);
    return 0;
}

