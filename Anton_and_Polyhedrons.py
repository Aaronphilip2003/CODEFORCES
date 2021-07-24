n=int(input())
sum=0
while(n!=0):
	shape=input()
	shape=shape.lower()
	if shape=="tetrahedron":
		sum=sum+4
	elif shape=="icosahedron":
		sum=sum+20
	elif shape=="cube":
		sum=sum+6
	elif shape=="dodecahedron":
		sum=sum+12
	elif shape=="octahedron":
		sum=sum+8
	n=n-1

print(sum)