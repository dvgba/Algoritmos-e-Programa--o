# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
codigo = int(input(""))
valorcompra = float(input(""))

if codigo == 2:
  valorpago = valorcompra - (valorcompra * 0.13)
  print("Valor total a ser pago: R$ %.2f" % valorpago)

elif codigo == 3:
  valorpago = valorcompra - (valorcompra * 0.07)
  print("Valor total a ser pago: R$ %.2f" % valorpago)

elif codigo == 1:
  valorpago = valorcompra
  print("Valor total a ser pago: R$ %.2f" % valorpago)

else:
  print("OPÇÃO INVÁLIDA!")