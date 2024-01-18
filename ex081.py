lista = []
cont = 0

while True:
    lista.append(int(input('Digite o valor desejado: ')))
    cont += 1 # Contador para contar quantos números foram digitados
    resp = str(input('Deseja continuar ? [S/N]')).upper().strip()
    while resp not in 'SsNn':
        print('Digite uma opção VÁLIDA !')
        resp = str(input('Deseja continuar ? [S/N]')).upper().strip()
    if resp in 'N':
        break
print(f'Foram digitados {cont} números')
print(f'A lista em de valores ordenada de forma decrescente é {sorted(lista,reverse= True)}')
# Loop/repetição para rastrear o número 5
pos = 0
cont5 = 0
posições5 = []
while pos < len(lista):
    if lista[pos] == 5:
        cont5 += 1
        posições5.append(pos+1)
    pos += 1
print(f'O valor 5 foi digitado {cont5} vezes, nas posições : {posições5}')



