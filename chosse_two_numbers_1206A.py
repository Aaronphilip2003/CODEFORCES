na=int(input())
a=input().split()
nb=int(input())
b=input().split()
a_int=[]
b_int=[]
for i in a:
	a_int.append(int(i))
for i in b:
	b_int.append(int(i))

all=a_int+b_int
ansi=[]
ansj=[]
for i in a_int:
	for j in b_int:
		sum=0
		sum=i+j
		if i in a_int and j in b_int and sum not in all:
			ansi.append(i)
			ansj.append(j)

print(ansi[0],ansj[0],end=" ")
