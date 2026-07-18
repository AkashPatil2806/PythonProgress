# A tuple is an immutable data type in python.

a = () # empty tuple
b = (1,) # tuple with only one element needs a comma
c = (1,7,2) # tuple with more than one element

print(type(a))
print(type(b))
print(type(c))

#Tuple Methods
# 1) d.index()
d = (1,12,32,34,65,47)
m=d.index(12)
print(m)

#2) e.count() is use to count the no of occurence of a value in string.
e = (1,12,32,34,65,47,12,32,12)
n = e.count(12)
print(n)
