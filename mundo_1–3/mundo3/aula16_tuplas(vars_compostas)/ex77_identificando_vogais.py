words = ('para', 'go', 'borbulhar')
vowels = ('a','e', 'i', 'o', 'u')
print('Vogais nas palavras', end = '')
for a in words:
	print(f'\n{a}: ', end = '')
	for b in vowels:
		if b in a:
			print(b, end = ' ')
print('\n')






#Outra forma
print('—' * 19)
print('Vogais nas palavras')
print('—' * 19, end = '')
words = ('para', 'go', 'borbulhar')
vowels = ('a','e', 'i', 'o', 'u')
for a in words:
	print(f'\n{a}: ', end = '')
	for letter in a:
		if letter in vowels:
			print(letter, end = ' ')
			