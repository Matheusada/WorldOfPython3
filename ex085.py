#LEMBRANDO QUE APENAS 1(UMA) ÚNICA LISTA!
lista = list()
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º número: '))
    if valor % 2 ==0:
        lista.insert(c,valor)
    if valor % 2 == 1:
        lista.insert(-c,valor) # Alinhando à esquerda
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados em ordem crescente é:')
for n in sorted(lista):
    if n % 2 ==0:
        print(f'[{n}]', end=' ')
print(f'\nOs valores ímpares digitados em ordem crescente é: ')
for n in sorted(lista):
    if n % 2 ==1:
        print(f'[{n}]',end =' ')



