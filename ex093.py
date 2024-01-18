# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
dadosCompleto = dict()
dados = dict()
pessoa = list()
cont = 0
while True:
    pessoa[cont].append(str(input('Nome: ')))
    dados['nome'] = pessoa[0]
    pessoa.clear()
    pessoa[cont].append(str(input('Sexo [M/F]')))
    dados['sexo'] = pessoa[1]
    pessoa[cont].append(int(input('Idade: ')))
    dados['idade'] = pessoa[2]
    cont += 1
    resp = str(input('Deseja cadastrar mais pessoas ? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
      break
print(dados)