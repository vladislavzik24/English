f = open('word.txt', 'r',  encoding='utf-8')
word = []

for line in f:
	word.append(line)
f.close()

word = sorted(word)

f2 = open('word_sort.txt', 'w', encoding='utf-8')

for i in range(len(word)):
	f2.write(str(i + 1) + '. ' + word[i])

print('Задание выполнено успешно')
