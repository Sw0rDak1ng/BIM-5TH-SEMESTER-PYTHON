"""Write a python program to find the sum of first n natural numbers using recursion."""
def sum_n(n):
    if n==1:
        return 1
    else:
        return n + sum_n(n-1)
n=int(input("Enter a number: "))
result=sum_n(n)
print("The sum of first", n, "natural numbers is", result)
