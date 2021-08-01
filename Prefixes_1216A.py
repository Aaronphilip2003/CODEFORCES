n=int(input())
string=input()
letters=[]
count=0
for i in string:
  letters.append(i)
for i in range(0,len(letters)-1,2):
  if letters[i]=="a":
    if letters[i+1]=="b":
      pass
    else:
      letters[i+1]="b"
      count+=1
  elif letters[i]=="b":
    if letters[i+1]=="a":
      pass
    else:
      letters[i+1]="a"
      count+=1
 
print(count)
print(''.join(map(str, letters)))
