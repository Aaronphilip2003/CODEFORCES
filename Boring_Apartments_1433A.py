numbers =[1,11,111,1111,2,22,222,2222,3,33,333,3333,4,44,444,4444,5,55,555,5555,6,66,666,6666,7,77,777,7777,8,88,888,8888,9,99,999,9999]
test =int(input())
while test !=0:
  call = int(input())
  counter = 0
  number_position = numbers.index(call)
  for i in range(0,number_position+1):
    counter = counter+len(str(numbers[i]))
  print(counter)
  
  test = test -1
