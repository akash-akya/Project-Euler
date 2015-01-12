import math
p=[2,]
f=1
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
	i=i+2
	f=1
	if(len(p)==10001):
		break
print(p[10000])