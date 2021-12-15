test_cases=int(input())

while test_cases!=0:

  number=int(input())
  count=0
  string_number=str(number)
  for i in string_number:
			if i!="0":
					count+=1
  print(count)
  if number<10:
    print(number)
  else:
  	for i in range(len(string_number)):
				if string_number[i]!="0":
						print(string_number[i]+(len(string_number)-(i+1))*"0",end=" ")
				else: 
						pass
  	print()
  test_cases-=1   

# 800 rated program
