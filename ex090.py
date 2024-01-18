# aluno = dict()
# aluno['nome'] = str(input('Digite o nome do aluno: '))
# aluno['media'] = float(input('Agora digite a média do aluno: '))
# if aluno['media'] >= 6:
#     situacao = aluno['situacao']='Aprovado'
# else:
#     situacao = aluno['situacao']='Reprovado'
# print(f'Nome é igual a: {aluno["nome"]}\nMédia é igual a: {aluno["media"]}\nSituação é: {aluno["situacao"]}')
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Agora digite a média do aluno: '))
if aluno['media'] >= 6:
    situacao = aluno['situacao']='Aprovado'
else:
    situacao = aluno['situacao']='Reprovado'
print(aluno)
for k,v in aluno.items():
     print(f'{k} é {v}')