""" Consider the following scenario. You have a list of students who are attending class "Python" and another list of students who are attending class "Web Application".Find the list of students who are attending “python” classes but not “Web Application”"""



# list of students who took python
Python = {"jason", "john", "jack","jade", "taylor", "tony"}

# list of students who took web
web = {"scott", "Sebastian", "steven", "taylor", "tony"}

# printing the common students who took both python and web using & operator

print("Students who take both python and web::",Python & web)

# storing the list of students who took only python to the variable 'a'
a = Python-web

# storing the list of students who took only web to the variable 'a'
b = web-Python

# printing the list of students who are not in common in both python and web
print("Students who are not in unique subjects::",a.union(b))

#python not web

print("Students who are in python but not in web::",a)