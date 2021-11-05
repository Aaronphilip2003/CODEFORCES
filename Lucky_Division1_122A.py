number=int(input())
copy=number
r=0
flag=0
numlist=[]
while number>0:
	r=number%10
	if r!=4 and r!=7:
		flag=1
		break
	number=number//10
if flag==0:
	print("YES")
else:
	if copy%7==0 or copy%4==0 or copy%74==0 or copy%47==0 or copy%444==0 or copy%777==0 or copy%774==0 or copy%747==0 or copy%477==0 or copy%447==0 or copy%474==0 or copy%744==0 :
		print("YES")
	else:
		print("NO")
