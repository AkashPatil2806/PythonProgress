# String is the data type in python indicated by the groups of letters enclosed in double quotes,
#  single quotes, or Triple Single quotes

name = ('Akash') 
name = ("Akash")
name = ('''Akash''')
print(name)


a = ("Akash")
# then
b = print(a[0:4])
                #  Here (Akash) is equivalent to the (0,1,2,3,,4) assigned string weights.
                # 0:4 includes respective assigned letters excluding (4) (h) because letter after collen ignored in python.
c = print(a[1:3])
 
d = ("amazing")
e = print(d[1:6:2])

f = "Sudhira"
g = print(f[1:4:2])  
                # This is called slicing.