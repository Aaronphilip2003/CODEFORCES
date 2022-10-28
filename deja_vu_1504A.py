test_cases = int(input())

while test_cases != 0:
    s = input()
    s_start = "a" + s
    s_end = s + "a"
    s_start_check = s_start[::-1]
    s_end_check = s_end[::-1]
    if s_start != s_start_check:
        print("YES")
        print(s_start)
    elif s_end != s_end_check:
        print("YES")
        print(s_end)
    else:
        print("NO")
    test_cases -= 1
