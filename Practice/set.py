"""curly bracket, unordered when output is printed, cant use index, no duplicate in use"""

thisset={'apple','banana','apple','cherry'}   
print(thisset)

#accessing the item in the set
thisset={'apple','cherry','banana'}
for x in thisset:
    print(x)

# adding items in the set

# 1)using add
thisset={'Apple','banana','cherry'}
thisset.add('orange')
print(thisset)

# 2) using update
thisset={'Apple','banana','cherry'}
tropical={'pineapple','mango','papaya'}
thisset.update(tropical)
print(thisset)

#removing items from the set
# 1) using the remove
thisset={'Apple','banana','cherry'}
thisset.remove('banana')
print(thisset)

# 2) using discard
# 3) using pop
# 4) using clear
# 5) using del keyword