red,blue=input().split()
red=int(red)
blue=int(blue)
redbuffer=red
bluebuffer=blue
fashionable=0

minsock=min(redbuffer,bluebuffer)

for i in range(0,minsock):
	fashionable=fashionable+1
	redbuffer=redbuffer-1
	bluebuffer=bluebuffer-1

print(fashionable,abs(int((red-blue)/2)))

