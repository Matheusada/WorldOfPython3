# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
anoAtual = date.today().year
idade = ' '
dadosTrabalhador = {'nome': str(input('Digite nome: ')),
                    'Ano Nascimento': int(input('Digite o ano de Nascimento: ')),
                    'Idade': idade,
                    'CTPS': int(input('CTPS: ')),
                    'Ano contratacao': int(input('Ano de contratação: ')),
                    'Salario': float(input('Salário (R$): '))
                    }
dadosTrabalhador['Idade'] = (anoAtual - dadosTrabalhador['Ano Nascimento'])
print(dadosTrabalhador)
