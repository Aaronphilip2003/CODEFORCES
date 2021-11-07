test_cases=int(input())
while test_cases!=0:
	numbers=input().split()
	numbers_int=[]
	for i in numbers:
		numbers_int.append(int(i))
	numbers_int.sort()
	print(numbers_int[0]*numbers_int[2])
	test_cases-=1
