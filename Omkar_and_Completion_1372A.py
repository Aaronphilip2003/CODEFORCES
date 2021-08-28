t=int(input())
e=40
while t!=0:
	l=[]
	n=int(input())
	while n!=0:
		l.append(e)
		n-=1
	print(*l, sep = " ")
	t-=1
