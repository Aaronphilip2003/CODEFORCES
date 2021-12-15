test_cases = int(input())
while test_cases!=0:
  x = int(input())
  k=1
  while k<x:
    k=k*2
  if k == x:
    print("no")
  else:
    print("yes")
  test_cases-=1
