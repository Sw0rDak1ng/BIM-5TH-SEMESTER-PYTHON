"""Write a python program to print the first n terms of fibonacci series using recursion."""
def fibo_series(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        series = fibo_series(n-1)
        series.append(series[-1] + series[-2])
        return series
num=int(input("Enter the number of terms to print in Fibonacci series: "))
result=fibo_series(num)
print("The first", num, "terms in the Fibonacci series are:", result)
