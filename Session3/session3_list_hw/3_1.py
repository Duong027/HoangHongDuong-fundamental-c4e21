import random
a = list('champion')
random.shuffle(a)
result = ' '.join(a)
print('The mixed order is:',result)

ask = input('Guess? ')
if ask == 'champion':
    print('Right')
else:
    print('Not right')
    while True:
        ask = input('Guess Again? ')
        
        if ask == 'champion':
            print('Right')
            break
        