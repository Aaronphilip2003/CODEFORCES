test_cases=int(input())

while(test_cases!=0):
	a,b,n,S=input().split()
	a=int(a)
	b=int(b)
	n=int(n)
	S=int(S)
	if S%n > b:
		print("NO")
	else:
	  if a*n+b>=S:
		  print("YES")
	  else:
		  print("NO")
		
	test_cases=test_cases-1