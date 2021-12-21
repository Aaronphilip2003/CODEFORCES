n=int(input())
badges=input().split()
badges_int=[]
 
for i in badges:
    badges_int.append(int(i))
    
badges_int.sort()
count=0
a=0
 
for i in range(1,n):
    if(badges_int[i]==badges_int[i-1]):
        badges_int[i]+=1
        count+=1
    elif badges_int[i]<badges_int[i-1]:
        a=badges_int[i-1]-badges_int[i]
        badges_int[i]+=a
        count+=a
        badges_int[i]+=1
        count+=1
 
print(count)
