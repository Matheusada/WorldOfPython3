#RACIOCÍNIO => O PRIMEIRO PARÊNTESE NÃO PODE SER ')' E O ÚLTIMO NÃO PODE SER '(', E O NÚMERO DE PARÊNTESES TEM QUE SER IGUAL !
expressao = list()
parenteses = list()
expressao.append(str(input('Digite a expressão desejada: ').strip()))
contPA = 0
contPF = 0
for i, v in enumerate(expressao):
    for i in v:
        if '(' in i:
            contPA += 1
            parenteses.append('(')
        if ')' in i:
            contPF += 1
            parenteses.append(')')
if contPA == contPF:
    for i, v in enumerate(parenteses):
        if parenteses[len(parenteses) - 1] == '('and v[i] == ')':
            print('Expressão está INCORRETA!')
            break
        else:
            print('A expressão está CORRETA!')
            break
else:
    if contPA != contPF:
        print('A expressão foi digitada incorretamente')

