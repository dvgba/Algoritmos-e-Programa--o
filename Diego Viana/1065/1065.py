a = []
for i in range(5):
    n = int(input())
    a.append(int(n))

l = 0
for j in range(5):
    if a[j] % 2 == 0:
        l += 1
print(l, "valores pares")