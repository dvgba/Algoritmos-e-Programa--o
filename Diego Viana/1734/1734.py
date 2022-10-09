fat = int(input())

res = 1
con = 1

while con <= fat:
    res *= con
    con += 1
print("%d! = %d" %(fat, res))