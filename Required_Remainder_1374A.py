test_cases=int(input())
while test_cases!=0:
	x,y,n=input().split()
	x=int(x)
	y=int(y)
	n=int(n)

	if n-n%x+y<=n:
		print(n-n%x+y)
	else:
		print(n-n%x-(x-y))
	test_cases-=1
