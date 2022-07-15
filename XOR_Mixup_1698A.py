test_cases=0
test_cases=int(input())
while test_cases!=0:
  ans=0
  n=int(input())
  nums=input().split()
  nums_int=[]
  for i in nums:
    nums_int.append(int(i))
  for i in range(0,len(nums_int)-1):
    ans^=nums_int[i]
  print(ans)
  test_cases-=1

