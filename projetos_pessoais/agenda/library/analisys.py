def rint(number):
    try:
        number = str(number).strip().replace(',', '.')
        number = int(number)
    except:
        return 0
    else:
        return number


def rhour(hour):
    hour = str(hour).strip()
    confirm = False
    if len(hour) == 5 and hour[2] == ':':
        try:
            if int(hour[:2]) <= 23 and int(hour[-2:]) < 60:
                return hour
        except:
            return confirm
    if confirm:
        return hour
    else:
        return confirm


def rlist(anlist):
    try:
        anlist = list(anlist)
    except TypeError:
        anlist = list()
    return anlist


def rtuple(antuple):
    try:
        return int(antuple)
    except:
        antuple = antuple.replace(',', '').replace(' ', '')
        antuple = list(antuple)
        confirm = True
        try:
            for element in antuple:
                if  not str(element).isnumeric():
                    confirm = False
                else:
                    element = int(element)
        except:
            return False
        else:
            if confirm:
                return tuple(sorted(set(antuple)))
            else:
                return False
