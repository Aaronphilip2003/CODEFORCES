def split(a):
	return [char for char in a]

n,t=input().split()
n=int(n)
t=int(t)
q=input()
index=[]
q_split=split(q)
for i in range(0,len(q_split)):
	if q_split[i]=='B':
		index.append(i)

while t!=0:
	for i in range(0,len(q_split)-1):
		if i in index:
			if q_split[i+1]=='G':
				q_split[i+1]='B'
				q_split[i]='G'
	index.clear()
	for i in range(0,len(q_split)-1):
		if q_split[i]=='B':
			index.append(i)
	t-=1
s=""
for i in q_split:
	s+=i
print(s)
