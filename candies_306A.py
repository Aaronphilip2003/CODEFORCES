candies , friends = input().split()
candies=int(candies)
friends=int(friends)
if candies%friends ==0:
  print(f"{str(candies//friends)} "*friends)
else:
  initial_candies = candies//friends
  remainder_candies= candies-(initial_candies*friends)
  list1=[initial_candies]*friends
  for i in range(0,remainder_candies):
    list1[i]=list1[i]+1
  for i in list1:
    print(i,end=" ")
