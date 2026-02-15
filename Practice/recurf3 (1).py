"""Write a python program to find the nth term of the Fibonacci series using recursion."""
def fibo(n):
    if n<=0:
        return "Invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
num=int(input("Enter the term number to find in Fibonacci series: "))
result=fibo(num)
print("The", num, "th term in the Fibonacci series is", result)
