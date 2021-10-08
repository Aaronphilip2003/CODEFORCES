test_cases=int(input())
while test_cases!=0:
	final_coins=[]
	multiplication=0
	people=int(input())
	coins=[]
	list_m=input().split()
	for i in list_m:
		coins.append(int(i))
	coins.sort()
	length=len(coins)
	for x in coins:
		multiplication=x*(length-coins.index(x))
		final_coins.append(multiplication)
	print(max(final_coins))
	
	test_cases-=1
