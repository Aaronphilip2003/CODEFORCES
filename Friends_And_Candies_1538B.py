t = int(input())
while t!=0:
	friends=int(input())
	candies = input().split()
	ideal_number=0
	candies_sum=0
	count=0
	if friends==1:
		print("0")
	else:
		for i in candies:
			candies_sum += int(i)
		if candies_sum % friends !=0:
			print("-1")
		else:
			ideal_number = candies_sum//friends
			for i in candies:
				if int(i) > ideal_number:
					count+=1
			print(count)
 
	t=t-1
