#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print(f'{"Analisador de Expressões":^50}')
print('-='*25)
expressao = []
expressao.append(str(input('Digite a expressão desejada (utilizando abertura/fechamento de  parênteses corretamente)\n>>>>')))
pos = 0
for i,v in enumerate(expressao):
    if v[i] != '(':
        print('Atenção ! Inicie a expressão com o parêntese correto')
    if v[len(v)-1] != ')':
        print('Finalize a expressão corretamente')
    else:
        print(f'PARABÉNS, a expressão "{v}" está com os parênteses corretos !')





