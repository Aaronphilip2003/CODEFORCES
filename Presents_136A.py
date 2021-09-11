n= int(input())
a=[int(x) for x in input().split()]
index=[]
for i in range(1,n+1):
  index.append(a.index(i)+1)
print(*index,sep=" ")
