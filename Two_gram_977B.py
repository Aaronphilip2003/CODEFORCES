def split(word):
	return[char for char in word]

n=int(input())
s=input()
s_list=split(s)
pair_list=[]
length=len(s_list)


for x in range(0,length-1):
	pair_list.append(s_list[x]+s_list[x+1])

max=0
ch=' '

for x in pair_list:
	if pair_list.count(x) > max:
		max=pair_list.count(x)
		ch=x


print(ch)
