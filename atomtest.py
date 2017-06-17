print('Hello, Django girls!')

print (1+2)
if 3>2:
    print('it works!')

if 5>2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

name = 'Hola'
if name == 'Hola':
    print('Hola Locas!')
elif name == 'Buenas':
    print('Hey Djangogirl')
else:
    print('ey joooo')
#this is so interesting shiat
volume = 1
if volume <20 or volume > 80:
    volume = 50
    print('thats better!')
#function

def hi():
    print('hey jo')
    print('que pasa?')

hi()

def hi(name):
    if name == 'Hola':
        print('Hola Locas!')
    elif name == 'Buenas':
        print('Hey Djangogirl')
    else:
        print('ey joooo')
hi("hola")

def hi(name):
    print('buenas' + name + '!')

hi ("seniora")
#LOOOOOOOOOPs
girls = ['Natalie', 'Bini', 'Monica', 'Matteo']
for name in girls:
    hi(name)
    print('Next girl')
    
