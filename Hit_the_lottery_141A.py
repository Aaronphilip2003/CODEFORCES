def split(a):
	return[char for char in a]



guest=input()
residence=input()
pile=input()

flag=100

guestlist=[]
residencelist=[]
pilelist=[]
combined=[]

guestlist=split(guest)
residencelist=split(residence)
pilelist=split(pile)
combined=guestlist+residencelist
combined.sort()
pilelist.sort()

if combined == pilelist:
	flag=1
else:
	flag=0

if flag==1:
	print("YES")
elif flag==0:
	print("NO")