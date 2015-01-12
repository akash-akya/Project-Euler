'''Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''


import math
total=0
for i in range(3,1000000):
	st=str(i)
	fa=0
	for j in range(len(st)):
		fa=fa+math.factorial(int(st[j]))
		if(fa>i):
			break
	if(fa==i):
		total=total+fa
print(total)