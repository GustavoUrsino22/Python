'''
Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), leu um
valor de temperatura em Fahrenheit e exibi-lo em Celsius
'''
valor_Fahrenheit = int(input('Escreva um valor para Fahrenheit : '))
celsius = int(5/9*(valor_Fahrenheit-32))
print('O valor de {} Fahrenheit equivale a {} Celsius'
      .format(valor_Fahrenheit,celsius))
