q = str(input('Type some phrase: ')).strip().lower()
print('The letter "a" appears {} times\nThe first time appears in position {}\n'
      'The last time appears in position {}'.format(q.count('a'), q.find('a') + 1, q.rfind('a') + 1))
