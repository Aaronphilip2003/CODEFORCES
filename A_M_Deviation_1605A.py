t=int(input())
for i in range(t):
	a,b,c=input().split()
	a=int(a)
	b=int(b)
	c=int(c)
	if (a+b+c)%3 == 0:
	 print("0")
	else:
		print("1")
