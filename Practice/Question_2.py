#wap to input a sentence and count the frequency of each words
sen = input("Enter a sentence: ")
words = sen.split()
for i in words:
    print(i, ":", words.count(i))
