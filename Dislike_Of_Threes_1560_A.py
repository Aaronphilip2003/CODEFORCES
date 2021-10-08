test_cases=int(input())
while test_cases!=0:
    list1=[]
    k=int(input())
    for i in range(1,10000):
        if i%3!=0 and i%10!=3:
            list1.append(i)
    print(list1[k-1])
    test_cases-=1
