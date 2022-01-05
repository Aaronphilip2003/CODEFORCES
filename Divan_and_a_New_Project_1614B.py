for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([a[i],i+1])
    arr.sort(reverse = True)
    ans = [0]*(n+1)
    for i in range(n):
        ans[arr[i][1]] = (i//2 + 1)*(-1 if i&1 else 1) 
    walk = 0
    for i in range(n):
        walk += 2*abs(ans[i+1])*a[i]
    print(walk)
    print(*ans)
