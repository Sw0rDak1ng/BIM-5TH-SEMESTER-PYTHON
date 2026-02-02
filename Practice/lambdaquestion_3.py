# given the list of names write a program using filter() with lambda to display only those name starting with 'R'

names=['Ram','Hari','Shyam','Rama']
withr_name= filter (lambda a:a.startswith('R'),names)
print(list(withr_name))
