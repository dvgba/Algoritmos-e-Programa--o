# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759
anoAtual = int(input(""))
valIni = float(input(""))
valSoma = 1015
contPercentual = 0.015
sumPercentual = 0.01

anos = anoAtual - 2006

if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")

elif anoAtual == 2006:
    print("Salário atual: R$:.2f"%(valIni))

elif anoAtual > 2006:
    porcentagem = contPercentual + sumPercentual
    Anterior = valIni + (contPercentual * valIni)

    for x in range(anos):
        calculo = Anterior + (Anterior * porcentagem)
        Anterior = calculo
        porcentagem += 0.01
    print("Salário atual: R$%.2f"%(calculo))