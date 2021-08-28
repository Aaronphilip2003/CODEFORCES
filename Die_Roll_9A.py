import math 
y,w = input().split()
y=int(y)
w=int(w)
maximum = max(y,w)
num=7-maximum
den=6
hcf=math.gcd(num,den)
print(f"{num//hcf}/{den//hcf}")
