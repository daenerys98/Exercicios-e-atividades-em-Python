from random import randint

numero_informado = 6
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('O número secreto é ? '))

print('numero secreto {} foi selecionado'.format(numero_secreto))
