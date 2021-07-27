def split(word):
	return [char for char in word]

test_cases=int(input())


while test_cases!=0:
	s=input()
	s2=""
	length=len(s)
	list_s=[]
	final_list=[]
	list_s=split(s)
	final_list=[]
	flag=False
	for x in range(1,len(list_s)-2):
		if x%2!=0:
			final_list.append(list_s[x])
		else:
			pass
	final_list.insert(0,list_s[0])
	final_list.insert(length-1,list_s[length-1])
	for x in final_list:
		s2=s2+x
	print(s2)

	test_cases=test_cases-1