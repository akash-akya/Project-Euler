# Special Pythagorean triplet
#Problem 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import math
for i in range(1,1000):
	for j in range(i,1000):
		k=math.sqrt(pow(i,2)+(pow(j,2)))
		#k=math.sqrt(l)
		if(i+j+k==1000):
			print(i*j*k)
			break