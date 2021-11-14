n = input()
line = input().split()
line_int=[]
for i in line:
    line_int.append(int(i))
minimum = min(line_int)
maximum = max(line_int)
count = line_int.index(maximum)
line_int.pop(count)
line_int.insert(0, count)
line_int.reverse()
count += line_int.index(minimum)
print(count)
