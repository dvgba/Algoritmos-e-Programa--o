valor = float(input(""))

if valor < 20:
    print("Valor de venda: R$%.2f " %(valor * 1.45))
else:
    print("Valor de venda: R$%.2f " %(valor * 1.30))