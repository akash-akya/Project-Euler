'''Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)'''

def tob(x):
    return int(bin(x)[2:])

su=0
for i in range(1,1000000):
	p=str(i)[::-1]
	if(i==int(p)):
		b1=tob(i)
		bp=str(b1)[::-1]
		if(b1==int(bp)):
			su=su+i
print(su)