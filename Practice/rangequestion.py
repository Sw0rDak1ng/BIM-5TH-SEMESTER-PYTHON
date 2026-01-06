#wap to input 2 number and print all numbers between them and find their sum
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
total = 0
for i in range(a, b + 1):
    print(i)
    total = total + i
print("Sum of the numbers is:", total)
