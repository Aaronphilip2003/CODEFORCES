n,k=input().split()
n=int(n)
k=int(k)

count=0
prob=0

for i in range (1,n+1):
	count=count+5*i
	if count>240-k:
		break
	else: 
		prob=prob+1

print(prob)
