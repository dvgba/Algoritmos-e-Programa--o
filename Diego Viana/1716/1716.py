# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
codigo = input("")
salario = float(input(""))

if (codigo != "A") and (codigo != "B") and (codigo != "C"):
    print("")
elif codigo == "A":
    novoSalario = salario * 1.10
    print("Novo salário: R$%.2f" % novoSalario)
elif codigo == "B":
    novoSalario = salario * 1.15
    print("Novo salário: R$%.2f" % novoSalario)
elif codigo == "C":
    novoSalario = salario * 1.20
    print("Novo salário: R$%.2f" % novoSalario)
