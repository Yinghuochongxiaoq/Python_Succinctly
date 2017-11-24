def say_hello():
    print('Hello every one.')
say_hello()
def say_hello(name='FreshMan'):
    print('Hello {}!'.format(name))
say_hello('FreshMan')
say_hello()
say_hello(name='FreshMan and JunJun')

def say_hello(first,last='FreshMan'):
    '''Say hello'''
    print('Hello {} {}!'.format(first,last))
say_hello('JunJun');
help(say_hello)

def even_or_odd(number):
    '''Datermine if a number is odd or even'''
    if  number%2==0:
        return 'Even'
    return 'Odd'
print(even_or_odd(9))

def get_name():
    '''Get and return a name'''
    name=input('What is your name?' )
    return name

def say_name(name):
    '''Say a name'''
    print('Your name is {}'.format(name))

def get_and_say_name():
    '''Get and display name'''
    name=get_name()
    say_name(name)
get_and_say_name()