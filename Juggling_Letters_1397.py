t = int(input())

while t!=0:
  n=int(input())
  rows =n
  count=[]
  l=[]
  maximum=0
  flag=True
  while n!=0:
    s=input()
    for i in s:
      l.append(i)
    n-=1
  for i in l:
    count.append(l.count(i))
  for i in count:
    if i%rows==0:
      flag = True
    else:
      flag=False
      break
  if flag == True:
    print("YES")
  else:
    print("NO")
  t-=1
