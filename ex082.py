#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas
lista = []
listaImpares = []
listaPares = []
while True:
    lista.append(int(input('Digite o número desejado: ')))
    resp = str(input('Deseja continuar ? [S/N]'))
    if resp in 'Nn':
        break
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0:
        listaPares.append(lista[pos])
    else:
        listaImpares.append(lista[pos])
    pos +=1
print(f'A lista digitada é: {lista}')
print(f'A lista de PAR digitadas é: {listaPares}')
print(f'A lista de ÍMPARES digitadas é: {listaImpares}')