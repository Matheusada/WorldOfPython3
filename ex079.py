#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list() # Pode ser valores= []
while True:
    valor = int(input('Digite o valor desejado: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com Sucesso !')
    else:
        print('Valor REPETIDO, não será adicionado !')
    resp = str(input('Deseja continuar ? [S/N]')).upper().strip()
    while resp not in 'SsNn':
        print('Digite uma OPÇÃO VÁLIDA!')
        resp = str(input('Deseja continuar ? [S/N]')).upper().strip()
    if resp == 'N':
        break
print(f'O valores Digitados EM ORDEM CRESCENTE E SEM REPETIÇÃO SÃO {(sorted(valores))}')