# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

qtdPessoas = 4
con90 = 0
idade = 0

while qtdPessoas > 0:
    idade1 = int(input(''))
    peso = float(input(''))

    if peso > 90:
        con90 = con90 + 1
        idade = idade1 + idade
        qtdPessoas = qtdPessoas - 1

    else:
        idade = idade1 + idade
        qtdPessoas = qtdPessoas - 1
media = idade / 4

print("Qtd pessoas > 90 Kg: %i" %con90)
print("Idade média: %.2f" %media)