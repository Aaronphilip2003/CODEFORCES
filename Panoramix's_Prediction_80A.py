list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
n,m=input().split()
n=int(n)
m=int(m)
index_n=0
if n in list1 and m in list1:
  index_n=list1.index(n)
  if list1.index(m) == list1.index(n)+1:
    print('YES')
  else:
    print('NO')
else:
	print("NO")
