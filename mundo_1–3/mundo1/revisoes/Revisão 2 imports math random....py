from math import sin, cos, tan, radians, factorial
angulo = int(input('Digite um ângulo: '))
a = radians(angulo)
print('''O seno do ângulo {} é {:.2f}
Seu cosseno é {:.2f}
Sua tangente é {:.2f}'''.format(angulo, sin(a), cos(a), tan(a)))
permu = str(input('Digite uma palavra: '))
n1 = int(input('Se uma letra se repete, digite quantas vezes: '))
n2 = int(input('Se houver outra faça o mesmo aqui (se não houver, digite 1): '))
n3 = int(input('Se houver outra faça o mesmo aqui (se não houver, digite 1): '))
n4 = int(input('Se houver outra faça o mesmo aqui (se não houver, digite 1): '))
mod = int(len(permu))
print(factorial(mod) / (factorial(n1) * factorial(n2) * factorial(n3) * factorial(n4)))
