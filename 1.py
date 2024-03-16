# Uma empresa de cartão de crédito envia suas faturas por email com
# a seguinte mensagem:
msg1 = print('Pagamento de Fatura')
nome_cliente = input('Qual é seu Nome Completo : ')
dia_vencimento = int(input('Qual é o Dia do Vencimento : '))
mes_do_vencimento = input('Qual é o Mês do Vencimento : ') 
valor_fatura = float(input('Qual é o Valor da Fatura : '))
dia_atual = int(input('Que dia é hoje ? : '))
if dia_atual < dia_vencimento:
    print('Olá {} !'.format(nome_cliente))
    print('Sua fatura com vencimento no dia {} do mês {} no valor de {} está em Aberto !'
    .format(dia_vencimento, mes_do_vencimento, valor_fatura))    
else:
    print('Olá {} !'.format(nome_cliente))
    print('Sua fatura com vencimento no dia {} do mês {} no valor de {} está Fechado !'
    .format(dia_vencimento, mes_do_vencimento, valor_fatura))