'''Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo usuário para
Km/h. Para tal, multiplique o valor em m/s por 3,6.'''
v_metros_p_segundos = int(input('Qual é a velocidade m/s :'))
#para transformar m/s em km/h basta dividir multiplicar por 3,6
v_Km_h = v_metros_p_segundos*3.6
velocidade_permitida = 80
print(v_Km_h,'Km/h')
if v_Km_h > velocidade_permitida:
    print('Calma calabreso!, Você está acima do limite de velocidade, MULTADO!')
elif v_Km_h >=50 and v_Km_h <= velocidade_permitida:
    print('Continue assim!')
elif v_Km_h <50:
    print('Vai para facha da direita ou acelera!!!')