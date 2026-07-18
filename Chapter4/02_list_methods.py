# List methods are differents functions of lists which are as follows
l1 = [21,0,32,546,54,56,7,87,743,]
# 1) l1.sort() This is used to arrange the list in ascending order.
l1.sort()
print(l1)

#2) l2.reverse() is used to order of the existing list.
l2 = [21,0,32,546,54,56,7,87,743,]
l2.reverse()
print(l2)

#3) l3.pop() is to used (pop) means to print the list excluding the value at the index position entered in the code.
l3 = [21,0,32,546,54,56,7,87,743,]
l3.pop(3)
print(l3)

#4) l4.append() is to add a new string in the end of the list.
l4 = ["Akash","28","True","3.14","Rahul"]
l4.append("Prakash")
print(l4)

# 5) l5.insert() is to insert add a new string in between of list members
l5 =  ["Akash","28","True","3.14","Rahul"]
l5.insert(1,"Patil")
print(l5)

# l6.remove() is to remove the particular value from the list.
l6 = [21,0,32,546,54,56,7,87,743,]
l6.remove(32)
print(l6)

# List are mutable data and changes can be done in values.
# As strings are immutable dat and changes cannot be done in values.