tabuada = int(input('Qual número deseja saber a tabuada? '))

print ('-' * 20 )    
for c in range (1, 11):
    print('{} x {:2} = {}'.format(tabuada, c, tabuada * c))
print ('-' * 20 )    

# Para não precisar fazer prints de 1 até 10 utiliza o for com o range fazendo as somas.
# Coloca do 1 até o 11, porque ele sempre come um no final, se colocar atpe 10 ele só soma até 9.
# O uso do '-' * 20 é opcional, só pra fazer charme kk
 