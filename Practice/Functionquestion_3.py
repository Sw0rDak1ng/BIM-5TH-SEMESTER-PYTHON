# wap to create a user defined function that takes a word as an argument
# and returns it reverse

def reverse(word):
    return word[::-1]
a = input('Enter the Word:')
print('Reverse word is:',reverse(a))
