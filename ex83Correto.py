expressao = str(input('Digite aqui sua expressão: '))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está correta !')
else:
    if len(lista) > 0:
        print('A expressão está incorreta !')
