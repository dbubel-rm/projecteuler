#include <stdio.h>
#include <math.h>

void fermatFactorization(int n, int * factors)
{
	double a = ceilf(sqrt(n));
	double b2 = a*a - n;
	while(ceilf(sqrt(b2)) != sqrt(b2))
	{
		a++;
		b2 = (a*a) - n;
	}
	double b = sqrt(b2);
	factors[0] = a-b;
	factors[1] = a+b;
}

int main()
{
	int factors[10];
	fermatFactorization(1337, factors);
	printf("f1 %i\n", factors[0]);
	for(int i = 0; i < 10; i++)
	{
		
	}
	return 0;
}