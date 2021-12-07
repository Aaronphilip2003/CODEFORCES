def split(a):
	return [char for char in a]

n=int(input())
wrong=input()
correct=input()

wrong_split=split(wrong)
correct_split=split(correct)

wrong_split_int=[]
correct_split_int=[]
sum=0

for i in wrong_split:
	wrong_split_int.append(int(i))

for i in correct_split:
	correct_split_int.append(int(i))

for i in range(0,n):
	sum+=min(10-abs(wrong_split_int[i]-correct_split_int[i]),abs(wrong_split_int[i]-correct_split_int[i]))

print(sum)

# 800 rated program
