n=int(input())

points=list(map(int,input().split()))
counter=0

for i in range(1,n):
	highest=0
	lowest=0
	for a in range (0,i):
		if points[i] > points[a]:
			highest=highest+1
		elif points[i]<points[a]:
			lowest=lowest+1
	if highest==i or lowest == i:
		counter=counter+1

print(counter)
	