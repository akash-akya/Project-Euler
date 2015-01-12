# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# ----- Convention ------
# 0  1  2  3  4  5  6
# Su Mo Tu We Th Fr Sa

d=[31,28,31,30,31,30,31,31,30,31,30,31]
d1=[31,29,31,30,31,30,31,31,30,31,30,31]
ns=0
r=2  # 1901 Jan 1 is Tuseday

for i in range(1901,2001):
	if(i%4!=0):
		for j in d:
			r=(r+j)%7
			if(r==0):
				ns=ns+1	
		print(i,ns)
	else:
		for j in d1:
			r=(r+j)%7
			if(r==0):
				ns=ns+1
		print(i,ns)
print(ns)

