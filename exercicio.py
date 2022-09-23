palavras_proibidas = {'política', 'religião', 'futebol'}
texto = [
    'joao gosta de politica e futebol'
    'miguel odeia praia'
    'carlos gosta de futebol'
    ]
    
for texto in texto:
    found = False
    for palavra in texto:
        if palavras in palavras_probidas:
            print('yes')
            
else:
    print('not')