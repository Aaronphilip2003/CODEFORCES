def split(a):
    return[char for char in a]

testcases=int(input())

while testcases!=0:
    n=int(input())
    students=input()
    count=0
    ans=0
    students_split=split(students)
    for i in range(n-1,-1,-1):
        if students_split[i]=="P":
            count+=1
        else:
            ans=max(ans,count)
            count=0
            
    
    print(ans)
    
    testcases-=1
    
