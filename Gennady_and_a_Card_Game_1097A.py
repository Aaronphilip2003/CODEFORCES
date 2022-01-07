def split(a):
	return [char for char in a]

s=input()
cards=input().split()
pos_zero=s[0]
pos_one=s[1]
flag=False

for i in cards:
	ch=split(i)
	if ch[1]==pos_one:
		flag=True
		break
	elif ch[0]=="A" and pos_zero=="A":
		flag=True
		break
	elif ch[0]=="K" and pos_zero=="K":
		flag=True
		break
	elif ch[0]=="Q" and pos_zero=="Q":
		flag=True
		break
	elif ch[0]=="J" and pos_zero=="J":
		flag=True
		break
	elif ch[0]=="T" and pos_zero=="T":
		flag=True
		break
	elif ch[0]=="2" and pos_zero=="2":
		flag=True
		break
	elif ch[0]=="3" and pos_zero=="3":
		flag=True
		break
	elif ch[0]=="4" and pos_zero=="4":
		flag=True
		break	
	elif ch[0]=="5" and pos_zero=="5":
		flag=True
		break
	elif ch[0]=="6" and pos_zero=="6":
		flag=True
		break
	elif ch[0]=="7" and pos_zero=="7":
		flag=True
		break
	elif ch[0]=="8" and pos_zero=="8":
		flag=True
		break
	elif ch[0]=="9" and pos_zero=="9":
		flag=True
		break

if flag==True:
	print("YES")
else:
	print("NO")

# 800 rated program
