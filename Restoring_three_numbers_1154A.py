a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)


num=[a,b,c,d]

num.sort()

print(num[3]-num[1],num[3]-num[2],num[3]-num[0])
