#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
parImpar = list()
listPares = list()
listImpares = list()
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor: ')) # As listas são MUTÁVEIS !
    if valor % 2 == 0:
        listPares.append(valor)
    else:
        listImpares.append((valor))
parImpar.append(listPares[:])
parImpar.append(listImpares[:])
print(f'Os pares em ordem crescente é {sorted(parImpar[0])}')
print(f'Os ímpares em ordem crescente é {sorted(parImpar[1])}')





