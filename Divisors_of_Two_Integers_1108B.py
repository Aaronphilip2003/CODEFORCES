number= int(input())
divisors = input().split()
divisors_int=[]
new_list=[]
third_list=[]
for i in divisors:
	divisors_int.append(int(i))
max_1 = max(divisors_int)
for i in divisors_int:
	if max_1%i==0 and i not in new_list:
		new_list.append(i)
for i in divisors_int:
  if divisors_int.count(i)>1 and i not in third_list:
    third_list.append(i)
for i in divisors_int:
  if i not in new_list:
    third_list.append(i)
max_2 = max(third_list)
print(max_1,max_2)
