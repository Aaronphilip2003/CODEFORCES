n=int(input())
l_list=[]
r_list=[]
while n!=0:
    l,r=input().split()
    l_list.append(int(l))
    r_list.append(int(r))
    n-=1

l_count0=l_list.count(0)
l_count1=l_list.count(1)
r_count0=r_list.count(0)
r_count1=r_list.count(1)

max_l=0
max_r=0

if l_count0>l_count1:
    max_l=0
elif l_count1>l_count0:
    max_l=1
else:
    max_l=0

if r_count0>r_count1:
    max_r=0
elif r_count1>r_count0:
    max_r=1
else:
    max_r=0
    
time_l=0
time_r=0

for i in l_list:
    if i!=max_l:
        time_l+=1

for i in r_list:
    if i!=max_r:
        time_r+=1

print(time_l+time_r)
