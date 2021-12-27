a=int(input()) # 4 3 2 1
b=int(input()) # 7 5 3 1
c=int(input()) #13 9 5 1

pass1=0

while True:
    if a>=1:
        a-=1
        if b>=2:
            b-=2
            if c>=4:
                c-=4
                pass1+=1
    else:
        break
                
            

print(pass1*7)
