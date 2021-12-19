n,k=input().split()

n=int(n)
k=int(k)

if k<=(n+1)//2:
    print(k*2-1)
else:
    print((k-(n+1)//2)*2)
