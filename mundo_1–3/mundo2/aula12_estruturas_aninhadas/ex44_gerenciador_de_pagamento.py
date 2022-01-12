pre = float(input('Valor pago: R$'))
print('''Métodos de pagamento
[1] À vista (dinheiro/cheque)
[2] À vista no cartão
[3] No cartão''')
sel = int(input('Digite uma das opções acima: '))
a, b = pre - (pre * 0.1), '10% de desconto'
if sel == 1:
    a, b = a, b
elif sel == 2:
    a, b = pre - (pre * 0.05), '5% de desconto'
elif sel == 3:
    parc = int(input('Em quantas parcelas serão divididas? '))
    if parc == 2 or parc == 3:
        a, b = pre + (pre * 0.05), '5% de juros'
    elif parc == 4 or parc == 5 or parc == 6:
        a, b = pre + (pre * 0.08), '8% de juros'
    elif parc == 7 or parc == 8:
        a, b = pre + (pre * 0.10), '10% de juros'
    elif parc == 9 or parc == 10:
        a, b = pre + (pre * 0.12), '12% de juros'
    elif parc == 11 or parc == 12:
        a, b = pre + (pre * 0.15), '15% de juros'
else:
    print('Digite uma opção válida')
if sel == 1 or sel == 2 or sel == 3:
    print('Sua compra terá {}, totalizando {}'.format(b, a))
