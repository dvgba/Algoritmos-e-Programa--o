# https://www.beecrowd.com.br/judge/pt/problems/view/1009
ID = input()
RE = float(input())
QTD = float(input())

BO = float(QTD * (15/100))

total = RE + BO

print("TOTAL = R$ %0.2f" %total)