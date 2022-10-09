# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
valHora = float(input(""))
hora = float(input(""))

salBruto = valHora * hora

imposto = salBruto * 0.11
inss = salBruto * 0.08
sindicato = salBruto * 0.05

saLiquido = salBruto - imposto - inss - sindicato

print("Salário bruto: R$%.2f" % salBruto)
print("Imposto: R$%.2f" % imposto)
print("INSS: R$%.2f" % inss)
print("Sindicato: R$%.2f" % sindicato)
print("Líquido: R$%.2f" % saLiquido)