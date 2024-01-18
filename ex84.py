#Exercício 84
dados = list()
listaGeral = list()
contPessoas = pesoMaior = pesoMenor =0
while True:
    dados.append(str(input('Digite o nome: ')))
    contPessoas += 1
    dados.append((float(input('Digite o peso (KG): '))))
    listaGeral.append(dados[:])
    dados.clear() #MUITO IMPORTANTE !!!!!!!!!
    resp = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('OPÇÃO INVÁLIDA !\nDeseja continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
for i, p in enumerate(listaGeral):
    if i == 0:
        pesoMaior = p[1]
        pesoMenor = p[1]
    else:
        if p[1] > pesoMaior:
            pesoMaior = p[1]
        if p[1] < pesoMenor:
            pesoMenor = p[1]
print(f'foram cadastradas {contPessoas} pessoas')
print(f'As pessoas mais pesadas com {pesoMaior} kg, são:', end= '')
for p in listaGeral:
    if p[1] == pesoMaior:
        print(f'[{p[0]}]')
print(f'As pessoas mais leves com {pesoMenor} kg, são:', end ='')
for p in listaGeral:
    if p[1] == pesoMenor:
        print(f'[{p[0]}]')

