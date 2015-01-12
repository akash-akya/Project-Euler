#Summation of primes
#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math
p=[2,]
f=1
s=2
i=3
while(1):
	for j in p:
		if(i%j==0):
			f=0;
			break
		if(j>math.sqrt(i)):
			break	
	if(f==1):
		p.append(i)
		s=s+i;
	i=i+2
	f=1
	if(i>2000000):
		break
print(s)