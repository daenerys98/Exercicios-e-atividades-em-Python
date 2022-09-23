def faixa_etaria(idade):
    
    if 0 <= idade < 18:
        return 'menor de idade'
    elif idade in range (18, 65):
        return 'adulto'
    elif idade in range (66, 100):
        return 'melhor idade'
    elif idade >=100:
        return 'centenaria'
    else :
        return 'data invalida'