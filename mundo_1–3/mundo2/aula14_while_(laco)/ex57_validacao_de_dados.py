c = ''
while c != 'sim':
    a = input('Digite seu sexo: ').strip().lower()
    b = ['masculino', 'feminino', 'transexual']    
    while a[:9] != b[0] and a[:8] != b[1] and a[:10] != b[2]:
        a = input('Digite um sexo válido: ').strip().lower()
    while c != 'sim' and c != 'não':
        if a[0] == 'm':
            c = input(f'Confirma que seu sexo é {b[0]}? ').strip().lower()
        elif a[0] == 't':
            c = input(f'Confirma que seu sexo é {b[2]}? ').strip().lower()
        elif a[0] == 'f':
            c = input(f'Confirma que seu sexo é {b[1]}? ').strip().lower()