expr = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressao VALIDA')
else:
    print('Expressao INVALIDA')