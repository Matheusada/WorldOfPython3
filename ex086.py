#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz1 = []
matriz2 = []
matriz3 = []
for n in range(0,3):
    matriz1.append(int(input(f'Digite o valor desejado na posição [0:{n}]: ')))
for n in range(0,3):
    matriz2.append(int(input(f'Digite o valor desejado na posição [1:{n}]: ')))
for n in range(0,3):
    matriz3.append((int(input(f'Digite o valor desejado na posição [2:{n}]: '))))
print('\n',[matriz1[0]],[matriz1[1]],[matriz1[2]],'\n',[matriz2[0]],[matriz2[1]],[matriz2[2]],'\n',[matriz3[0]],[matriz3[1]],[matriz3[2]],)


