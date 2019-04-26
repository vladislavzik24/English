f = open('text.txt', 'r',  encoding='utf-8')
words = []

for line in f:
		for i in line.split():
			if i not in words:
				if len(i) > 4:
					if (';' or ',' or '.' or ':') in i:
						i = i[:len(i)-1]
					
					words.append(i)
					
f.close()

words = sorted(words)
f2 = open('text2.txt', 'w', encoding='utf-8')
for i in words:
	f2.write(i + '\n')