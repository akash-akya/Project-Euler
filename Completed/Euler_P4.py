# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# solved on 17/02/14 ~akash

pii=0
pij=0
h=0
for i in range(100,999):
	for j in range(100,999):
		m=j*i
		k=(str(m))[::-1]
		k=int(k)
		if(k==m and k>h):
			h=k
print(h)	
