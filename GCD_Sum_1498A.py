import math

def sumOfDigits(a):
    sum=0
    while(a>0):
        r=a%10
        sum+=r
        a=a//10
    return sum

test_cases=int(input())

while test_cases!=0:
    n=int(input())
    sum=sumOfDigits(n)
    ans=0
    while True:
        if(math.gcd(n,sumOfDigits(n)))>1:
            ans=n
            break
        else:
            n+=1
    print(ans)  
    test_cases-=1
