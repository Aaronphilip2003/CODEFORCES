q=int(input())

while q!=0:
    l1,r1,l2,r2=input().split()
    l1=int(l1)
    r1=int(r1)
    l2=int(l2)
    r2=int(r2)
    ansi=0
    ansj=0
    
    print(l1,end=" ")
    
    if l1!=l2:
        print(l2)
    
    else:
        print(r2)
    
    q-=1
