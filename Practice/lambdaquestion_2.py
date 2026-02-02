#using the filter 
numbers=[1,2,3,4,5]
even_numbers=filter(lambda a:a%2==0,numbers)
print(list(even_numbers))

# for odd 
odd_numbers=filter(lambda a:a%2!=0,numbers)
print(list(odd_numbers))