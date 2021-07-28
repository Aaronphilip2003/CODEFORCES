def split(a):
	return[char for char in a]


a1,a2,a3,a4=[int(x) for x in input().split()]
s=input()
sum=0

s_split=split(s)

for x in s_split:
	
	if x=="1":
		sum+=a1
	elif x=="2":
		sum+=a2
	elif x=="3":
		sum+=a3
	elif x=="4":
		sum+=a4

print(sum)
