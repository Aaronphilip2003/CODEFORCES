def split(s):
	return [char for char in s]
s=input()
s=s.lower()
s_list=split(s)
s1=""
while s_list.count("a")!=0 or s_list.count("e")!=0 or s_list.count("i")!=0 or s_list.count("o")!=0 or s_list.count("u")!=0 or s_list.count("y")!=0:
  for i in s_list:
	  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
 		  s_list.remove(i)
i=0
while (i!=len(s_list)):
	s_list.insert(i,'.')
	i+=2
for i in s_list:
	s1+=i
print(s1)
