# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input())
qtdHora = float(input())
valHora = 10.00
salMin = 1192.40


salario_hora_extra = qtdHora * valHora
bruto = (salMin*3) + salario_hora_extra

if bruto > 2500.00:
    INSS = bruto * 0.20
    imposto = bruto * 0.12
    liquido = bruto - (INSS + imposto)
elif bruto <= 2500.00:
    INSS = bruto * 0.05
    liquido = bruto - INSS

print('Nome: %s' % nome)
print("Salário bruto: R$%.2f" % bruto)
print("Salário líquido: R$%.2f" % liquido)