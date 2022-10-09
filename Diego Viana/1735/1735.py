# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735
start = int(input())
stop = int(input())
while start >= stop:
    print(start)
    start = start - 1
print("Fogo!")