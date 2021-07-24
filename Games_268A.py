teams=int(input())
homelist=[]
awaylist=[]
x=0
i=0

n=teams


while(n!=0):
	home,away=(input().split())
	home=int(home)
	away=int(away)
	homelist.append(home)
	awaylist.append(away)
	n=n-1



for i in range(len(homelist)):
  if homelist[i] in awaylist:
    x += awaylist.count(homelist[i])

print(x)
