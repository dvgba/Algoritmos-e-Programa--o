def clear():
    print("\n" * 40)
while True:
    print()
    n = 1
    total = 0
    while True:
        preco = float(input(""))
        n += 1
        total += preco
        if preco == 0:
            break
    print("Total: R$ {:.2f} ".format(total))
    dinheiro = float(input())
    print("Troco: R$ {:.2f}".format(dinheiro - total))
