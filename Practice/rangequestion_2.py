#wap to input 2 number,print all numbers and find the sum of odd and even numbers
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
evensum=0
oddsum=0
for i in range(a,b):
    print(i)
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
print("Sum of even numbers:",evensum)
print("Sum of odd numbers:",oddsum)
