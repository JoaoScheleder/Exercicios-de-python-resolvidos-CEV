def notas(*num,sit=False):
    dicionario = {}
    dicionario["total"] =len(num)
    maior = menor = media = 0
    for c in range(len(num)):
        media += num[c]
        if c == 0:
            menor = num[0]
            maior = num[0]
            dicionario["maior"] = maior
            dicionario["menor"] = menor
        else:
            if num[c] > maior:
                maior = num[c]
                dicionario["maior"] = maior
            elif num[c]< menor:
                menor = num[c]
                dicionario["menor"] = menor
    dicionario["media"] = media/len(num)
    if dicionario["media"]<6:
        dicionario["situaçao"] = 'RUIM'
    else:
        dicionario["situaçao"] = 'BOA'
    if sit :
        return dicionario
    else:
        del dicionario["situaçao"]
        return dicionario


print(notas(5,6,1,7,10,0))