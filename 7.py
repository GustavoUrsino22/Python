bloco = int(input('Qual bloco você mora, 1,2,3,4 ? :  '))
par_ou_impar = bloco % 2 
if par_ou_impar == 0:
    print('A caixa de água que abasteceu seu bloco foi: CAIXA A')
else:
    print('A caixa de água que abasteceu seu bloco foi: CAIXA B')