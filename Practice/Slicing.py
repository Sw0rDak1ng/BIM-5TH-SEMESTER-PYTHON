# Extracting all characters
s = "Hello World"
s1 = s[:]
print(s1)

# Specifying start index
s = "Hello world"
s1 = s[2:]
print(s1)

# Specifying start and end index
s = "Hello Word"
s1 = s[2:5]
print(s1)

# Specifying start, end, and step
s = "Hello Word"
s1 = s[0:10:2]
print(s1)

# Specifying negative step
s = "Hello"
s1 = s[::-1]
print(s1)

# Using f-strings
price = 50
print(f'price of the noodles is rs{price}')
print(f'Price of the noodles is Rs{round(50.2)}')

# Using str.format()
price = 50
txt = 'Price is Rs{}'
print(txt.format(price))

item = 'Noodles'
price = 20
txt = 'Price of {} is Rs{}'
print(txt.format(item, price))

item = 'Noodles'
price = 20
txt = 'Price of {0} is Rs{1}'
print(txt.format(item, price))

txt = 'I am from {country}'
print(txt.format(country='Nepal'))
