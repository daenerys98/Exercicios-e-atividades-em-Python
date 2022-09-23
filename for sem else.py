PALAVRAS_PROIBIDAS =  ['futebol', 'religião', 'política']
textos = [
    'João ama futebol e religião',
    'canva é legal',
    'na política tudo é dificil'
    ]
    
for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
           print('palavra proibida:', palavra, texto)
           found = True
           break

if not found:
    print('texto autorizado:',texto)