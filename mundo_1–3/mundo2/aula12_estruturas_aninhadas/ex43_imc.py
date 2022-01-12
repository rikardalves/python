alt = float(input('Digite aqui sua altura (m): '))
letra = str(alt)
# print(letra)__Para entender 0 sem . no início
if letra.find('.') == 2:
    alt = alt / 10
elif letra.find('.') == 3:
    alt = alt / 100
elif letra.find('.') == 4:
    alt = alt / 1000
elif letra[:4] == '0.00':
    alt = alt * 1000
elif letra[:3] == '0.0':
    alt = alt * 100
elif letra[0] == '0':
    alt = alt * 10
peso = float(input('Digite aqui o seu peso (kg): '))
cal = peso / alt ** 2
print('Seu IMC é de {:.2f}'.format(cal))
if cal < 18.5:
    print('Você está a baixo do peso')
elif 18.5 <= cal < 25:
    print('Você está com o peso ideal')
elif 25 <= cal < 30:
    print('Você está com sobrepeso')
elif 30 <= cal < 35:
    print('Vecê está com obesidade de grau 1')
elif 35 <= cal < 40:
    print('Você está com obesidade de grau 2')
else:
    print('Você está com obesidade mórbida')
# Outro método linha 10 a 15
# elif letra[0] == '0':
#     alt = alt * 10
#     if letra[2] == '0':
#         alt = alt * 10
#         if letra[3] == '0':
#             alt = alt * 10
