def prime(a):
  flag = False
  count=0
  if a > 1:
    for i in range(1, a+1):
      if (a % i) == 0:
        count+=1
  if count==2:
    flag=True
  else:
    flag=False
  return flag
 
t=int(input())
while t!=0:
  n=int(input())
  n2=n
  copy=n
  d=n-1
  x=1
  rc=[]
  matrix=[]
  d=0
  while prime(copy-1+x)==False or prime(x)==True:
    x+=1
  for i in range (0,copy):
    elist = []
    for j in range(0,copy):
      if i==j:
        elist.append(x)
      else:
        elist.append(1)
    print(*elist, sep=" ")
  t-=1
