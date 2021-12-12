n=int(input())
test=n
ans=0
initial_one=[1]*n
while test!=1:
	next_row=[1]
	for i in range(1,n):
		next_row.append(initial_one[i]+next_row[i-1])
	initial_one=next_row
	ans=next_row[len(next_row)-1]
	test-=1
if(n==1):
	print(1)
else:
	print(ans)

# import math
 
# number = int(input())
# if number == 1:
#   print(1)
# else:
#   n = 2*(number-1) - 1
#   answer = math.factorial(n)//(math.factorial(n- (number-1))*math.factorial(number-1))
#   print(answer*2)
# Soham's method using pascal's triangle
