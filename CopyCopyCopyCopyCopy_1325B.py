test_cases=int(input())
while(test_cases!=0):
	n=int(input())
	a=[int(x) for x in input().split()]
	copy=[]
	k=0
	a_set=set(a)
	print(len(a_set))
	test_cases=test_cases-1