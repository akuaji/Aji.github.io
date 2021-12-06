from random import randint
corret = 0

for _ in range(20):
    a = randint(0, 100)
    b = randint(0, 100)
    rd = a + b
    print(a, "+", b, "=")
    r = int(input())

    if r == rd:
        corret += 1
