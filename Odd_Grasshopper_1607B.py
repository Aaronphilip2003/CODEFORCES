test_cases = int(input())
while test_cases!=0:
  x,n =input().split()
  x=int(x)
  n=int(n)
  mod=n%4
  l= n-mod+1
  while l<=n:
    if x%2==0:
      x = x-l
    else:
      x = x+l
    l+=1
  print(x)
  test_cases-=1
