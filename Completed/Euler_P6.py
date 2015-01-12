#Sum square difference

#Problem 6
#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


#solved on 17/02/14 ~ akash hiremath

s=0
p=0
for i in range(1,101):
	s=s+i**2
	p=p+i
p=p**2
print(p-s)
