n=int(input())
sum=[]

while n!=0:
    list=input().split()
    list_int=[]
    for i in list:
        list_int.append(int(i))
    
    sum_students=0
    
    for i in list_int:
        sum_students+=i
    
    sum.append(sum_students)
    n-=1

thomas=sum[0]


sum.sort(reverse=True)

for i in range(len(sum)):
    if sum[i]==thomas:
        print(i+1)
        break
