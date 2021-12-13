rounds=int(input())
count_m=0
count_c=0
while rounds!=0:
	m,c=input().split()
	m=int(m)
	c=int(c)

	if m>c:
		count_m+=1
	elif c>m:
		count_c+=1
	rounds-=1

if count_m>count_c:
	print("Mishka")
elif count_c>count_m:
	print("Chris")
else:
	print("Friendship is magic!^^")
