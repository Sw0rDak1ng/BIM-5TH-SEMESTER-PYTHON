"""x=lambda a: a*a
print(x(5))"""
"""x=lambda a,b: a+b
print(x(5,10))"""

"""map ()
Syntax: map(function, iterable)
it returns a list by applying the function to each item of iterable (list, tuple etc.)

Without using lambda function:
def square(n):
    return n*n
numbers=[1,2,3,4,5]
squared_numbers=list(map(square,numbers))
print(list(squared_numbers))

With using lambda function:
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda a:a*a,numbers))
print(list(squared_numbers))

"""
"""Given the list of numbers, use map() and function with lamba to increase salary by 25 %. """
"""sal=[1000,2000,3000,4000,5000]
increased_sal=list(map(lambda s: s+0.25*s, sal))
print(list(increased_sal))"""

"""Filter() 
Syntax: filter(function, iterable)
--> It returns a list by applying the given function to each item of iterable object which satisfies the given criteria.
EXample:
numbers=[2,3,15,7,9,6]
even_numbers=list(filter(lambda a: a%2==0, numbers))
print(list(even_numbers))

"""
"""numbers=[2,3,15,7,9,6]
even_numbers=filter(lambda a: a%2==0, numbers)
print(list(even_numbers))
odd_numbers=filter(lambda a: a%2!=0, numbers)
print(list(odd_numbers))"""

"""Given the list of names, write a program using filter() with lambda to display only those names that start with 'R'.
names=['Ram','Shyam','Rita','Sita','Ramesh']
r_names=filter(lambda n: n.startswith('R'), names)
print(list(r_names))"""

"""3. Sort()
Syntax: sort(key=function)
--> It is used to sort the list of items according to key specified by the function.
Example:
students=[('Ram',20,'Ktm'),('Hari',21,'Bkt'),('Sita',22,'Lpt')]
students.sort(key=lambda x: x[1])  #sort by age
print(students)
"""
students=[('Ram',20,'Ktm'),('Hari',23,'Bkt'),('Sita',22,'Lpt')]
students.sort(key=lambda x: x[1])  #sort by age
print(students)