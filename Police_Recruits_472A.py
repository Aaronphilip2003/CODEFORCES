n = int(input())

li = list(map(int, input().split()))

hired = untreated = 0

for el in li:
    if el > 0:
        hired += el
        continue
    if hired > 0 and el < 0:
        hired -= 1
        continue
    if el < 0:
        untreated += 1

print(untreated)