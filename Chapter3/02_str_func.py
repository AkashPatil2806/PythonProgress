# String functions : There various types of string functions to carry out various functions easily

# len()  It is used to calculate the length of the string.

a = "Akash" 
print(len(a))
 
# endswith() It is use to check whether the string ends with mention characters.

b = "Tony Stark"
print(b.endswith("ark"))

# startswith() vice versa of endswith()
C = "Pepper Potts"
print(b.startswith("Pep"))
                    
# count() counts total number of occurence of a particular letter in a string
d = "Bruce Banner"
print(d.count("b"))
print(d.count("B"))
                    # Here the output of lowercase "b" will 0 as there ae no such character of small b, hence the output will be 0.

# capitalize() capitalizes first letter of first word.

e = "i am iron man."
print(e.capitalize())

# find() is use to find the index of the character.
f = "Peter"
print(f.find("e"))

# replace() is use to replace the letter.
g = "Natasha"
print(g.replace("a","aa"))