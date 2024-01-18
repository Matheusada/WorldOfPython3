import random
import time
listaCompleta = []
numerosSorteados = []
quantJogos = int(input('Quantos jogos deseja? '))
cont = 0
while cont < quantJogos:
    print(f'\nJogo {cont+1}:',end=' ')
    for c in range(1,7):
        n = random.randint(1,60)
        if c == 1:
            numerosSorteados.append(n)
        elif c != 1:
            n = random.randint(1, 60)
            if n not in numerosSorteados[:]:
                numerosSorteados.append(n)
            else:
                n = random.randint(1, 60)
                while n in numerosSorteados:
                    n = random.randint(1, 60)
                    if n not in numerosSorteados:
                        numerosSorteados.append(n)
    listaCompleta.insert(cont, numerosSorteados[:])
    print(f'{sorted(numerosSorteados)}', end=' ')
    time.sleep(1)
    numerosSorteados.clear()
    cont += 1
print(f'\nBOA SORTE!')



