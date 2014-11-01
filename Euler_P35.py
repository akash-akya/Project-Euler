import math
li=[]
for i in range(3,200,2):
	ro=int(math.sqrt(i))
	f=1
	for j in range(3,ro+1,2):
		if(i%j==0):
			f=0
			break
	if(f==1):
		li.append(i)
print(li)
print(len(li))

#li=[123]
for i in li:
	n=i
	for j in range(len(str(i))):
		r=n%10
		n=(n//10)+r*(10**(len(str(i))-1))
		#print(n,r)
		if(j not in li):
			li.remove(i)
			break
print(li)
print(len(li))

