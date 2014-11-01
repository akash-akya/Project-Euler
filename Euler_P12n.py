s=0
h=0
for i in range(500,1000):
	s=s+i
	c =0
	k=s//2
	for i in range(1,k):
		if(s%i == 0):
			c += 1
	if(c>=500):
		print(s)
		h=c
		break
	if(h<c):
		h=c
print(s,h)