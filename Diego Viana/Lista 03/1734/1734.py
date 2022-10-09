# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

fat = int(input())

res = 1
con = 1

while con <= fat:
    res *= con
    con += 1
print("%d! = %d" %(fat, res))