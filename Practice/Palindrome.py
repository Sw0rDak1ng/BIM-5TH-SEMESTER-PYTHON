a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

for n in range(a, b + 1):
    i = n
    rev = 0

    while i > 0:
        r = i % 10
        rev = rev * 10 + r
        i = i // 10

    if rev == n:
        print(n)
