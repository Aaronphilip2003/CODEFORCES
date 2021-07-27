n=int(input())
list_initial=[int(x) for x in input().split()]

ones=list_initial.count(1)
twos=list_initial.count(2)
threes=list_initial.count(3)
totalteams=min(ones,twos,threes)
print(totalteams)

indices1 = []
for i in range(len(list_initial)):
	if list_initial[i] == 1:
		indices1.append(i+1)

indices2 = []
for i in range(len(list_initial)):
	if list_initial[i] == 2:
		indices2.append(i+1)

indices3 = []
for i in range(len(list_initial)):
	if list_initial[i] == 3:
		indices3.append(i+1)

x=0
while totalteams!=0:
	print(indices1[x],indices2[x],indices3[x])
	x=x+1
	totalteams=totalteams-1
  