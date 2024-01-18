#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list() #ou [] apenas
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º valor desejado: '))
    valores.append(min,valores and max,valores)
    pos = 0
    while pos < len(valores):
        if n <= valores[pos]:
            valores.insert(pos, n)
            break #Teve esse break por conta de se fazer a leitura de cada número..., sem lista pronta!
        pos += 1
print(valores)