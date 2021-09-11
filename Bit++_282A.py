n=int(input())
count=0
while n!=0:
  string=input()
  if string == "++X" or string=="X++":
    count+=1
  else:
    count-=1
  n=n-1
print(count)
