h=1
n=1
for i in range(837799,1000000,2):
	k=i
	c=0
	while(k>1):
		if(k%2==0):
			k=k/2
		else:
			k=3*k+1
		c=c+1
	if(c>h):
		h=c
		n=i
print(n)

