"""Write a python program to take list of numbers as input and to return a tuple of first and last numbers in the list."""

values=input("enter a few numbers for the tuple::")
list=values.split(",")
tuple=tuple(list)
print('Tuple : ', tuple)
print('list: ', list)

print('first element of a tuple is: ',tuple[0])

print('last element of a tuple is: ',tuple[-1])


