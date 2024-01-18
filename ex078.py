valores = []
maiorV = 0
menorV = 0
for v in range(0,5):
    valores.append(int(input(f'Digite o {v+1}º valor desejado para colocar na lista: ')))
    if v == 0:
        maiorV = valores[v]
        menorV = valores[v]
    else:
        if valores[v] > maiorV:
            maiorV = valores[v]
        if valores[v] < menorV:
            menorV = valores[v]
print('-='*25)
print(f'Você digitou os seguintes valores {valores}')
print(f'O MAIOR valor digitado foi {maiorV} e está nas posições: ', end=' ')
for i, v in enumerate(valores):
    if valores[i] == maiorV: # Melhor colocar v == maiorV => ora, valores[i] = v !
        print(i + 1)
print(f'O MENOR valor digitado foi {menorV} e está nas posições: ', end=' ')
for i, v in enumerate(valores):
    if valores[i] == menorV: # Melhor colocar v == menorV
        print(i + 1)
