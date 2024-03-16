'''Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu
perímetro. Faça também para um triângulo.'''

print('Calcular a área e o perímetro do retângulo')
altura_retangulo = int(input('Qual é a altura do retângulo : '))
comprimento_retangulo = int(input('Qual é o comprimento do retângulo : '))
area_retangulo = altura_retangulo*comprimento_retangulo
perimetro_retangulo = (altura_retangulo*2)+(comprimento_retangulo*2)
print('A área do retângulo é {} e o perímetro é {}'.format(area_retangulo,perimetro_retangulo))
altura_triangulo = int(input('Qual é a altura do triangulo'))
comprimento_triangulo = int(input('Qual é a base do triângulo : '))
lado_triangulos1 = int (input('Qual é o lado1 do triângulo : '))
lado_triangulo2 = int(input('Qual é a lado2 do triângulo : '))
area_triangulo = (altura_triangulo*comprimento_triangulo)/2
perimetro_triangulo = comprimento_triangulo+lado_triangulos1+lado_triangulo2
print('A área do triângulo é {} e o perímetro é {}'.format(area_triangulo,perimetro_triangulo))
