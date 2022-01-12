from random import randint
from time import sleep
value = randint(1, 5)
print('Try to guess the chosen value!')
ans = int(input('Type a value between 1 and 5: '))
print('Processing...')
sleep(1.25)
if ans == value:
    print("You're right")
else:
    print(f'You missed, the correct number is {value}. Better luck next time')
