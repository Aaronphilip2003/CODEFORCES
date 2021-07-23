length=int(input())
word = input()
word=word.lower()
list1=[]
unique_list=[]

def split(word):
	return [char for char in word]

list1=split(word)

for x in list1:
	if x not in unique_list:
		unique_list.append(x)

if len(unique_list) == 26:
	print("YES")
else:
	print("NO")



