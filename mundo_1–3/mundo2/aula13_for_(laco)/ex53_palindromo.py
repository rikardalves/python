frase = str(input('Digite uma frase e veja se é um palíndromo: ')).split()
juntas = ''.join(frase)
inv = ''
print(juntas[::-1])
for palavra in range(len(juntas) -1, -1, -1):
    inv += juntas[palavra]
if inv == juntas:
    pren = ''
else:
    pren = ' não'
print(f"A frase invertida fica '{inv}', sendo assim ela{pren} é um palíndromo")