'''Number spiral diagonals
Problem 28
Published on Friday, 11th October 2002, 10:30 pm; Solved by 55346
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?'''

# Old code :
'''s=1
s4=1
i=1
r=3
while(r<=1001):
	s1=s4+2*i
	s2=s1+2*i
	s3=s2+2*i
	s4=s3+2*i
	s=s+s1+s2+s3+s4
	i += 1
	r += 2
print(s)'''


s=1
s4=1
i=1
r=3
while(r<=1001):
	for j in range(1,5):
		s=s+s4+(2*i*j)
	s4=s4+4*i*2
	i += 1
	r += 2
print(s)

