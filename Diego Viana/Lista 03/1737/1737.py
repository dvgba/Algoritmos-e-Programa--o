# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

n = 1
soma = 0
y = int(input())

if y <= 0:
    print("Informe uma quantidade > 0!")


else:
    while n <= y:
        x = float(input())
        soma = soma + x
        n = n + 1
    print("Soma dos números informados: %.2f" %(soma))