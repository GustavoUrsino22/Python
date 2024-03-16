'''
Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:
Exemplo 1:
Entrada de Dados:
Digite um número inteiro: 78615
Saída de Dados: 1
'''
num_int = int(input('Escreva um número inteiro : '))
if num_int <10:
    print('Esse número não tem dezena')
else:  
    dezena = (num_int // 10) % 10
    print('A dezena é:', dezena)
