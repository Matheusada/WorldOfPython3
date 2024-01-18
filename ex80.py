#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list() #ou [] apenas
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º valor desejado: '))
    if c == 0 or n > valores[len(valores)-1]:# valores[len(valores)-1]= valores[-1]# #comparação com o primeiro e último número e -1 por conta do fatiamento ... 1 a mais
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(valores)

