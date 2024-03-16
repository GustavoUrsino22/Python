#Preciso criar um algoritmo que valide 2 dados de uma pessoa e cheque com nossos requisitos.
req_idade = 18
req_altura = 1.75
idade = 0
altura = 0

idade = int(input('Qual é sua idade? : '))
altura = float(input('Qual é sua altura? : '))

validação = idade >= req_idade and altura >= req_altura
if validação is True:
    print('Pode passar, requisitos mínimos atingidos')
else:
    print('Não pode passar, requisitos mínimos não atingidos')