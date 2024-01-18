# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = dict()
galera = list()
somaIdade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite um valor VÁLIDO, M ou F !')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
        if resp in 'SsNn':
            break
        print('Digite um valor VÁLIDO, S ou N !')
    if resp == 'N': # Break aqui é em relação ao principal lá em cima (atenção a identação)
        break
print(galera)
print('=-'* 30)
print(f'Pessoas cadastradas: {len(galera)}')
media = somaIdade / len(galera)
print(f'Média de idade: {media}')
print(f'Lista com mulheres: ', end= '')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end= ' ')
print()
print(f'Lista com pessoas com idade acima da média:  ', end= '')
for p in galera:
    if p['idade'] >= media:
        print(p['nome'])

