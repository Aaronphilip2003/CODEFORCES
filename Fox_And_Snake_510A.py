n,m=input().split()
n=int(n)
m=int(m)
k=1
for i in range(1,n+1):
	for j in range(1,m+1):
		if i%2==0 and i%4!=0 and j!=m:
			print(".",end="")
		elif i%2==0 and i%4!=0 and j==m:
			print("#",end="")
		elif i%2==0 and i%4==0 and j!=1:
			print(".",end="")
		elif i%2==0 and i%4==0 and j==1:
			print("#",end="")
		else:
			print("#",end="")
	print()

