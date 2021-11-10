def sumDig(a):
	r=0
	sum=0
	while(a>0):
		r=a%10
		sum+=r
		a=a//10
	return sum


n=int(input())
ans=0

while True:
	sumNumber=0
	sumNumber=sumDig(n)
	if sumNumber%4==0:
		ans=sumNumber
		break
	n+=1

print(n)
