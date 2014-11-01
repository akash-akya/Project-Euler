// Power digit sum
// Problem 16
// 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

// What is the sum of the digits of the number 21000



#include<stdio.h>

int main()
{
	int a[302],i,j,f,c=0,s=0;

	for(i=0;i<302;i++)
		a[i]=0;

	a[0]=1;
	for(i=0;i<1000;i++)
		for(j=0;j<302;j++)
		{
			f=(a[j]*2)/10;
			a[j]=((a[j]*2)%10)+c;
			c=f;
		}

	for(i=0;i<302;i++)
		s=s+a[i];

	printf("%d",s);
	return 0;
}