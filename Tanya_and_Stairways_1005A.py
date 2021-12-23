n=int(input())
stairs=input().split()
stairs_int=[]
count=0
stairs_climbed=[]
for i in stairs:
    stairs_int.append(int(i))
 
for i in range(0,len(stairs_int)):
    if stairs_int[i]==1:
        count+=1
 
for i in range(1,len(stairs_int)):
    if stairs_int[i]==1:
        stairs_climbed.append(stairs_int[i-1])
 
stairs_climbed.append(stairs_int[len(stairs_int)-1])
 
print(count)
print(*stairs_climbed,sep=" ")
