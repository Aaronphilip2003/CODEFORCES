import math

def perfect_Square(a):
    root=math.sqrt(abs(a))
    
    if int(root+0.5)**2==a:
        return True
    else:
        return False

n=int(input())

numbers=input().split()

numbers_int=[]

for i in numbers:
    numbers_int.append(int(i))

numbers_int.sort(reverse=True)

for i in numbers_int:
    check=perfect_Square(i)
    
    if check==False:
        print(i)
        break
