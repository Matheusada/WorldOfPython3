lista = []
c = 0
for n in range(1, 8):
    valor = int(input(f"Digite o {n}o. número: "))
    if valor % 2 == 0:
        lista.append(valor)
    else:
        lista.insert(0, valor) # alinhando à esquerda
        c += 1

print(f"Os valores digitados foram: {lista}")
print(f"Os valores ímpares em ordem crescente foram: {sorted(lista[0:c])}")
print(f"Os valores pares em ordem crescente foram: {sorted(lista[c:])}")