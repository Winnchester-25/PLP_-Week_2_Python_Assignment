my_list =[]

# Add an element to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)

#Extend my_list with another list: [50, 60, 70].

my_list.append(50)
my_list.append(60)
my_list.append(70)
print(my_list)

#Remove the last element from my_list.
del my_list[-1]
print(my_list)

#Sort my_list in ascending order.

my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list..
print(my_list[3])