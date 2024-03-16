#Contador de Segundos
segundos_entrada = int(input('Digite o número de segundos : '))
dias = int(segundos_entrada/86400)
horas = int(segundos_entrada/3600)
minutos = int(segundos_entrada/60)
segundos = int(segundos_entrada)
print('Você passou {} dias, {} horas, {} minutos e {} segundos correndo na praia'
      .format(dias,horas,minutos,segundos))
print('Organizando')
print(dias,'dias')
print(horas,'horas')
print(minutos,'minutos')
print(segundos,'segundos')