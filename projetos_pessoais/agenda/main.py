from library.actions import *
from library.interface import *
from datetime import datetime

time = datetime.today().strftime('%H:%M')
routine = 'routine.txt'
content = ['Agendar compromisso', 'Ver rotina', 'Sair']
week = ['Domingo', 'Segunda-feira', 'Terça-feira', 
        'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 
        'Sábado', 'Todos os dias']

if not havefile(routine):
    addfile(routine)

# Criação interfaceinterface e interação
while True:
    header('\033[1mROTINA\033[m')
    body(content, 'y', 'c')
    line()
    
    # Escolha do usuário
    while True:
        choice = rint(input(c('Opção: ', 'g', 1)))
        if choice <= 0 or choice > 3:
            print(c('Digite uma opção válida', 'r'))
        else:
            break
    
    # Acões de cada escolha
    if choice == 1:
        header(c('AGENDAR', 'n', 1))
        body(week)
        line()
        
        # Resultado opção 1
        while True:
            dayweek = limit(rtuple(input(c('Dia(s) da semana: ', 'g', 1))), 8)
            if not dayweek:
                print(c('Digite o(s) número(s) correspondente(s) com o que deseja', 'r'))
            else:
                if '8' in str(dayweek):
                    dayweek = ('1', '2', '3', '4', '5', '6', '7')
                break
        
        while True:
            hour = rhour(input(c('Horário(HH:MM): ', 'g', 1)))
            if hour == False:
                print(c('Digite um horário válido', 'r'))
            else:
                if rfile(routine, hour) and rweek(routine, dayweek):
                    print(c('Este horário na {} está oculpado', 'r'))
                    continue
                break
        
        while True:
            description = str(input(c('Programação: ', 'g', 1)))
            nory = confirm(c('Confirmar? ', 'y', 1))
            if nory:
                break
        wrtfile(routine, dayweek, hour, description)
    break
