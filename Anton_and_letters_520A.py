def split(word):
	return [char for char in word]

word=input()
word=word.replace("{","")
word=word.replace("}","")
word=word.replace(","," ")
word=word.replace(" ","")

wordlist=[]
wordlist=split(word)
uniquelist=[]

for i in wordlist:
	if i not in uniquelist:
		uniquelist.append(i)

print(len(uniquelist))