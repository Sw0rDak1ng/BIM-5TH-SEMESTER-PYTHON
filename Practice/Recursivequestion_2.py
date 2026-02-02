# to find the sum of first n natural numbers (using recursion)

def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n - 1)

num = int(input("Enter the Number: "))
result = natural_sum(num)
print("Result:", num, result)
