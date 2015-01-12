# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

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
	if(i>775146):
		break

for i in p:
	if(600851475143%i==0):
		h=i
print(h)