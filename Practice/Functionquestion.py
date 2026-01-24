# wap to create a user defined function that takes a number as an argument
# and checks odd/even takes input from the user

def check(a):
    if a % 2 == 0:
        print('Even')
    else:
        print('Odd')

x = int(input('Enter the Number: '))
check(x)
