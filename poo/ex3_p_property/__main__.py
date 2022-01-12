from lib import *


a = Product( 'melancia', 'r$24, 08')
print(a.value)
a.value = a.increase(50)
print(a.value)
a.reduction(50)
print(a.value)
print(a.name)