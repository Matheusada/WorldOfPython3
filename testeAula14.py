n = 1
somaPar = 0
somaImpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            somaPar += 1
        else:
            somaImpar +=1
print('Você digitou {} números PARES e {} números ÍMPARES '.format(somaPar, somaImpar))