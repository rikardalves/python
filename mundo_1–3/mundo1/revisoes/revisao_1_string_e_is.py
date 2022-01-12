# Manipulação de string, análise, transformação, div e junção
# Função is
print('Instruções: fazer um programa que leia algo', end=''
                                                         '(2 ou mais conteúdos) que for digitado e '
                                                         'retorne todas as suas características.''''
Converta o valor lido para string,remova espaços irrelevantes e faça a análise completa do mesmo.
Questões:\n1) Forme outro(s) conteúdo(s) utilizando a "frase" inicial
2) Remova apenas um conteúdo da "frase", retornado-a sem esse conteúdo
3) Torne essa "frase" em maiúscula
4) Forme uma nova palavra usando como base a frase, e adicione a ela
''')
# Blank
Algo = input('Digite algo aqui: ').strip()
print(f'É alfanumérico? {Algo.isalnum()}\nÉ numérico? {Algo.isnumeric()}\nÉ um espaço? {Algo.isspace()}\n'
      f'É decimal? {Algo.isdecimal()}\nÉ maiúscula? {Algo.isupper()}\nÉ title? {Algo.istitle()}\n'
      f'É ascii? {Algo.isascii()}\nÉ minúscula? {Algo.islower()}')
mudou = str(Algo)
cont_tudo = len(mudou)
encontrar0 = mudou.find('a')
encontrar1 = mudou.rfind('a')
contar = mudou.count('a')
em = 'a' in mudou
print('''Quantos caracteres tem? {}
Onde há o primeiro a? {}
Onde há o último a? {}
Quantos "a"? {}'''.format(cont_tudo, encontrar0, encontrar1, contar))
r = mudou.split()
novo = '{}'.format(mudou.replace(r[1], 'LesGO')).split()
sem1 = novo[0], ' '.join(novo[2:len(novo)])
sem2 = str(' '.join(sem1))
print(f"{' '.join(novo)}\nSem uma palavra: {sem2}")
print(f'Frase maiúscula: {sem2.upper()}')
pro = sem2[sem2.find('o')], sem2[sem2.find('u')], sem2[sem2.find('ç')], sem2[sem2.find('a')]
print(sem2 + ' '.join(pro))
