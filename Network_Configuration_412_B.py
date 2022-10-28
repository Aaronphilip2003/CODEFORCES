n,k=input().split()
n=int(n)
k=int(k)
speed=[int(x) for x in input().split()] 
speed.sort(reverse=True)
print(speed[k-1])
