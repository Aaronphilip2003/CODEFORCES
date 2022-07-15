test_cases = 0
test_cases = int(input())
while test_cases != 0:
    a, b = input().split()
    c, d = input().split()
    steps = 0
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    sum = a + b + c + d
    if sum == 0:
        steps = 0
    elif sum == 4:
        steps = 2
    else:
        steps = 1
    print(steps)
    test_cases -= 1
