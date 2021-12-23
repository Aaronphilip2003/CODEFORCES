test_cases=int(input())
 
while test_cases!=0:
    n=int(input())
    string=input()
    
    count=0
    for i in range(len(string)-1,-1,-1):
        if string[i]==')':
            count+=1
        else:
            break
    
    if 2*count>n:
        print("Yes")
    else:
        print("No")
    
    test_cases-=1
