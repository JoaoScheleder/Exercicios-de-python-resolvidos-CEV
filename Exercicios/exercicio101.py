from datetime import date
hoje = date.today().year

def voto(a):
    idade = hoje - a
    if idade >= 18 and idade <=70:
        x = 'VOTO OBRIGATORIO!!'
        return x
    elif idade <18 and idade >15 or idade >70:
        x = 'VOTO FACULTATIVO'
        return x
    elif idade <16 :
        x = 'VOTO NEGADO'
        return x

ano = int(input('Digite o ano em que nasceu'))
print(voto(ano))