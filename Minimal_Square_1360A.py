n=int(input())

while(n!=0):
	a,b=input().split()
	a=int(a)
	b=int(b)
	max1=max(2*b,a)
	max2=max(2*a,b)
	ans=min(max1,max2)
	print(ans*ans)
	n=n-1