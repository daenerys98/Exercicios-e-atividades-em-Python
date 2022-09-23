from time import sleep
delay = 4 
print('========================== Jogo de dados ========================') 

print('Em alguns segundinhos o computador irá dizer qual número do dado foi escolhido. \N{grinning face}')

print ('Caso ambos deem iguais você venceu')

sleep(delay)

import random
nosso = random.randint(1,6)
computador = random.randint(1,6)

print(nosso)
print(computador)

if nosso == computador:
    print('Você acertou')
else:
    print('tente novamente')    
