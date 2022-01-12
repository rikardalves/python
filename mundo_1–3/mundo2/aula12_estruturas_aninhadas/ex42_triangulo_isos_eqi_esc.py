s1 = int(input('Valor do segmento 1: '))
s2 = int(input('Valor do segmento 2: '))
s3 = int(input('Valor do segmento 3: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Esses segmentos podem formar um triângulo', end=' ')
    if s1 == s2 == s3:
        print('equilátero')
    elif s1 != s2 != s3:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Esses segmentos não formam um triângulo')
