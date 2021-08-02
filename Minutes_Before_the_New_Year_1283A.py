test_cases=int(input())

while(test_cases!=0):
	hours,minutes=input().split()
	hours=int(hours)
	minutes=int(minutes)
	total_minutes=60-minutes
	total_hours=(23-hours)*60
	print(total_hours+total_minutes)
	test_cases-=1