print('===========  Lojinha da Karol ===========')

preço = float(input('Digite aqui o valor da sua compra: '))
print ('''Formas de pagamento            
          [1] à vista dinheiro
          [2] à vista cartão
          [3] 2x no cartão
          [4] 3x no cartão ou mais''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    total = preço - (preço * 10/100)
    
elif opcao == 2:
    total = preço - (preço * 5/100)
    
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Total de compras {} e fica duas parcelas de {}.'.format(preço, parcela))
    
elif opcao == 4:
     total = preço + (preço * 20/100)
     totalparcelas = int(input('quantas parcelas: '))
     parcela = total / totalparcelas
     print ('Valor total de compra {} em parcelas de {}x ficará o total de {} reais, COM JUROS'.format(total, parcela, totalparcelas))
     
    
print('sua compra de {:.2f} reais ficará por {:.2f}'.format(preço, total))
