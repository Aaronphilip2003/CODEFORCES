total1=0
total2=0
total3=0
total4=0
d1,d2,d3=input().split()
d1=int(d1)
d2=int(d2)
d3=int(d3)
total1=d1+d2+d3
total2=2*d1+2*d2
total3=2*d2+2*d3
total4=2*d1+2*d3

print(min(total1,total2,total3,total4))
