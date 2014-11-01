def div(n):
	for x in xrange(math.sqrt(n),2,-1):
		if()



s=0
for i in range(1,10000):
	s=s+i
	c=1
	for j in range(2,(s//2)):
		if(s%j==0):
			c=c+1
	if(c>500):
		print(s)
		break