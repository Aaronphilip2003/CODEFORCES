n=int(input())
countx=0
county=0
countz=0
while(n!=0):
	x,y,z=input().split()
	x=int(x)
	y=int(y)
	z=int(z)
	countx+=x
	county+=y
	countz+=z
	n-=1
if countx==county==countz==0:
	print("YES")
else:
	print("NO")
