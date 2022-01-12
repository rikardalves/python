def readname(msg):
    while True:
        try:
            name = str(input(msg)).strip().title()
            if name == '':
                print('\033[31mDigite um nome\033[m')
                continue
        except:
            print('\033[31mOcorreu um erro validar o nome\033[m')
            continue
        else:
            return name


def truename(msg):
    try:
        name = str(msg).strip().title()
        return name
    except:
        print('\033[31mOcorreu um erro validar o nome\033[m')


def filexists(file):
    try:
        read = open(file, 'rt')
        read.close()
    except FileNotFoundError:
        return False
    else:
        return True


def addfile(name):
    try:
        create = open(name, 'wt+')
        create.close()
    except:
        print('\033[31mHouve um erro ao criar o arquivo\033[m')
    else:
        print(f'\033[32mArquivo {name} criado com sucesso\033[m')


def readfile(name):
    file = 0
    try:
        file = open(name, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        for line in file:
            line = line.split(';')
            line[1] = line[1].replace('\n', '')
            print(f'{line[0]: <30}{line[1]: >10} anos')
    finally:
        file.close()


def saveinfo(file, name='Unknown', age=0):
    write = 0
    try:
        write = open(file, 'at')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        try:
            write.write(f'{name};{age}\n')
        except:
            print('\033[31mErro ao adicionar conteúdo ao arquivo\033[m')
        else:
            print(f'\033[32mCadastro feito com sucesso\033[m')
    finally:
        write.close()


def repet(file, name):
    myfile = ''
    have = False
    try:
        name = str(name).strip().title()
    except:
        print('\033[31mOcorreu um erro desconhecido\033[m')
    try:
        myfile = open(file, 'rt')
        readline = myfile.readline()
        while readline:
            if str(readline[:-4]) == name:
                have = True
                break
            else:
                readline = myfile.readline()
        return have
    except:
        print('\033[31mErro ao ler conteúdo do arquivo\033[m')
    finally:
        myfile.close()


def surname(name):
    answer = ''
    try:
        name = truename(name)
        if len(name.split()) == 1:
            answer = False
        else:
            answer = True
    except:
        print('\033[31mOcorreu um erro desconhecido\003[m')
    finally:
        return answer
