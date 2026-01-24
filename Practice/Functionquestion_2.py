# wap to check a user defined function that takes two numbers as argument
# and print all numbers from first to last

def printnum(x, y):
    for i in range(x, y + 1):
        print(i)
a = int(input('Enter the first Number: '))
b = int(input('Enter the Second Number: '))
printnum(a, b)
