#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

f=1
f2=0
s=0
w=0
while(s<4000000):
	s=f2+f
	f=f2
	f2=s
	#print(s)
	if(s%2==0):
		w=w+s
print(w)