# Tuple

#====================================

''' A tuple is an ordered, immutable collection that allows duplicate values.'''
# Create tuple
numbers = (10, 20, 30, 40, 20)

print("Tuple:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("Slice:", numbers[1:4])

# Count
print("Count of 20:", numbers.count(20))

# Index
print("Index of 30:", numbers.index(30))

# Length
print("Length:", len(numbers))

# Membership
print("20 in tuple:", 20 in numbers)

# Loop
for value in numbers:
    print(value)

# Tuple unpacking
employee = (101, "John", "Sales")

eid, name, dept = employee

print("ID:", eid)
print("Name:", name)
print("Department:", dept)

# List to tuple
my_list = [100, 200, 300]
my_tuple = tuple(my_list)

print("List to Tuple:", my_tuple)

# Tuple to list
new_list = list(numbers)

print("Tuple to List:", new_list)