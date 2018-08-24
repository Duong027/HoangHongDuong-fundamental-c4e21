import random

chars = ['champion','meticulous','hexagon']
c = random.choice(chars)
a = list(c)

random.shuffle(a)
result = ' '.join(a)
print('The mixed order is:',result)

ask = input('Guess? ')
if ask == 'champion':
    print('Right')
elif ask == 'hexagon':
    print('Right')
elif ask == 'meticulous':
    print('Right')

else:
    print('Not right')
    while True:
        ask = input('Guess Again? ')
        
        if ask == 'champion':
            print('Right')
            break
        elif ask == 'hexagon':
            print('Right')
            break
        elif ask == 'meticulous':
            print('Right')
            break