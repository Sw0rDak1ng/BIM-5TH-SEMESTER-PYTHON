#add
thistuples=('apple','banana','cherry')
y=list(('orange'))
y.append('orange')
thistuple=tuple(y)

#remove
thistuple=('apple','banana','cherry')
y=list(thistuple)
y.remove('apple')
thistuple=tuple(y)

#change
x=('apple','banana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)
