def rfloat(value):
    try:
        value = float(value)
    except:
        try:
            if ',' in str(value) or ' ' in str(value):
                value = float(value.replace(',', '.'))
        except:
            value = False
    return value


def have_create(file):
    try:
        with open(file, 'rt') as archive:
            return True
    except:
        with open(file, 'x') as archive:
            return False
    
    
def writedoc(file, content):
    with open(file, 'at+') as archive:
        archive.write(content)
