# 1)Type= Use to indicate type of a variable. The basic type operators in Python are: type() and isinstance().
a = 5
print("Type of a =", type(a))

b = 5.5
print("Type of b =", type(b))

c = "Hello"
print("Type of c =", type(c))

a ="1.1"
b = float(a)
print("Type of b =", type(b))  
# Types like strings can be converted to other types using type conversion functions like int(), float(), str(), etc.
#But some types cannot be converted to other types, for example, a string containing non-numeric characters cannot be converted to an integer or float.