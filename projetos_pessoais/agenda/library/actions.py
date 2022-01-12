def limit(ipt, value):
    try:
        if ipt.__class__ == tuple:
            if int(max(ipt)) > value or int(min(ipt)) < 1:
                return False
            else:
                return ipt
        else:
            if ipt > value or ipt < 1:
                return False
            else:
                return ipt
    except:
        return False



def confirm(msg):
    from library.interface import c
    while True:
        question = str(input(msg)).strip().lower()
        if question == 'sim':
            return True
        elif question.replace('ã', 'a') == 'nao':
            return False
        else:
            print(c('Digite corretamente', 'r'))


def havefile(file):
    try:
        tryopen = open(file, 'rt')
        tryopen.close()
    except FileNotFoundError:
        return False
    else:
        return True


def rfile(file, content):
    try:
        read = open(file, 'rt')
        for line in read:
            if str(content) in line:
                return True
            else:
                save = False
        return save
    except:
        return False
    finally:
        read.close()


def rweek(file, content):
    try:
        read = open(file, 'rt')
        for line in read:
            if str(content) in line[:line.find('-') + 1]:
                return True
            elif line[:line.find('-') + 1] in str(content):
                return True
            else:
                save = False
        return save
    except:
        return False
    finally:
        read.close()


def addfile(name):
    try:
        file = open(name, 'wt+')
        file.close()
    except:
        return False
    else:
        return True


def wrtfile(file, dayweek, time, description):
    try:
        write = open(file, 'at')
        write.write(f'{dayweek}-{time};{description}\n')
    except:
        return False
    finally:
        write.close()
