test_cases=int(input())
while(test_cases!=0):
	n=int(input())
	a=[int(x) for x in input().split()]
	length=len(a)
	pointer1=0
	pointer2=length-1
	finallist=[]
	finallisteven=[]

	if length%2!=0:
		while(pointer2!=(length//2)-1):
			finallist.append(a[pointer1])
			finallist.append(a[pointer2])
			pointer1+=1
			pointer2-=1
		finallist.pop()
		print(*finallist,sep=" ")
	elif length%2==0:
		while(pointer2!=(length//2)-1):
			finallisteven.append(a[pointer1])
			finallisteven.append(a[pointer2])
			pointer1+=1
			pointer2-=1
		print(*finallisteven,sep=" ")
		test_cases-=1

