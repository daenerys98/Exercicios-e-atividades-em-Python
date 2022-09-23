from time import sleep
delay = 1

import random

print ('============= Joguinho =============')
e = print ('''      Escolha sua opção
          [ 1 ] PAPEL 
          [ 2 ] TESOURA
          [ 3 ] PEDRA''')
escolha = int(input('Qual opção você deseja?'))
itens = ('papel', 'tesoura', 'pedra')
r2 = random.randint(1,3)

print('Jo')
sleep (delay)
print('KEN')
sleep (delay)
print('PO!!!')
sleep(delay)

if escolha != r2:
    print('Você perdeu, o computador escolheu {}'.format(r2))
    
elif escolha == r2:
    print('Você vence!')