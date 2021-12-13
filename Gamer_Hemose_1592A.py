test_cases=int(input())

while test_cases!=0:
	n,H=input().split()
	n=int(n)
	H=int(H)
	strength=[]
	strength=[int for int in input().split()]
	strength_int=[]
	for i in strength:
		strength_int.append(int(i))
	strength_int.sort()
	count=0
	buffer=1
	while(H>0):
		H=H-strength_int[-buffer]
		if buffer==1:
			buffer=2
		else:
			buffer=1
		count+=1
	print(count)
	test_cases-=1

  # time limit exceeded
  # i really do not understand the point of the solution its so mathematical and literally impossible to know
