a1,a2,a3,a4=input().split()

a1=int(a1)
a2=int(a2)
a3=int(a3)
a4=int(a4)



if a1+a2==a3+a4 or a2+a3==a1+a4 or a1+a3==a2+a4 or abs(a1-a2)==abs(a3-a4) or abs(a2-a3)==abs(a1-a4) or abs(a1-a3)==abs(a2-a4) or abs(a1+a2)==abs(a3-a4) or abs(a2+a3)==abs(a1-a4) or abs(a1+a3)==abs(a2-a4) or abs(a1-a2)==a3+a4 or abs(a2-a3)==a1+a4 or abs(a1-a3)==a2+a4:
    print("YES")
else:
    print("NO")
