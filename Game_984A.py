n=int(input())
numbers=input().split()
numbers_int=[]
for i in numbers:
    numbers_int.append(int(i))

numbers_int.sort(reverse=True)

k=0

while n!=1:
    if k==0:
        del numbers_int[:1]
        k=1
    elif k==1:
        del numbers_int[-1]
        k=0
    n-=1

print(numbers_int[0])
