test_cases=int(input())
while test_cases!=0:
  capacity=[int(x) for x in input().split()]
  waste=[int(x) for x in input().split()]
  if waste[0]>capacity[0] or waste[1]>capacity[1] or waste[2]>capacity[2]: 
    print("NO")
  else:
    capacity[0]=capacity[0]-waste[0]
    capacity[1]=capacity[1]-waste[1]              #1 2 5
    capacity[2]=capacity[2]-waste[2]              #1 2 3 1 1
    waste[0]=0                                         
    waste[1]=0
    waste[2]=0
    if capacity[0]!=0:
      if waste[3]!=0:
        if waste[3]>capacity[0]:
          waste[3]=waste[3]-capacity[0]
          capacity[0]=0
        else:
          capacity[0]=capacity[0]-waste[3]
          waste[3]=0
    if capacity[1]!=0:
      if waste[4]!=0:
        if waste[4]>capacity[1]:
          waste[4]=waste[4]-capacity[1]
          capacity[1]=0
        else:
          capacity[1]=capacity[1]-waste[4]
          waste[4]=0
    if waste[3]+waste[4]>capacity[2]:
      print("NO")
    else:
      print("YES")        
  test_cases=test_cases-1