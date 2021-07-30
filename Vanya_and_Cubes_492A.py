def sum(n):
	sum1=0
	for i in range (1,n+1):
		sum1+=i
	return sum1

cubes=int(input())
sum1=0
sum2=0
k=1
while(sum2<=cubes):
	sum1=sum(k)
	sum2+=sum1
	k=k+1
	sum1=0
print(k-2)
