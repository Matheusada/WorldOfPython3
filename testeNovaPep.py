s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print(f'Você digitou o número {n} e a soma dos números digitados foi {s}')