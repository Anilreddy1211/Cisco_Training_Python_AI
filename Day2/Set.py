
# SET IN PYTHON

# Creating a set
numbers = {10, 20, 30, 40, 20, 30}

print("Set:", numbers)

empty_set = set()
print("Empty Set:", empty_set)

# To Add one element to set
numbers.add(50)
print("After add():", numbers)

# To Add multiple elements to set
numbers.update([60, 70, 80])
print("After update():", numbers)

#To  Remove an element from set
numbers.remove(20)
print("After remove():", numbers)

#To Remove/Discard an element from set
numbers.discard(100)   # No error if element doesn't exist
print("After discard():", numbers)

# Check membership
if 30 in numbers:
    print("30 is present")

print("Length:", len(numbers))

print("Elements:")
for value in numbers:
    print(value)

# SET OPERATIONS


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print("Union:", A | B)
print("Union:", A.union(B))

# Intersection
print("Intersection:", A & B)
print("Intersection:", A.intersection(B))

# Difference
print("Difference:", A - B)
print("Difference:", A.difference(B))

# Symmetric Difference
print("Symmetric Difference:", A ^ B)
print("Symmetric Difference:", A.symmetric_difference(B))

# Remove duplicate elements from list


numbers_list = [10, 20, 20, 30, 30, 40, 40]

unique_numbers = set(numbers_list)

print("Original List:", numbers_list)
print("Unique Values:", unique_numbers)

# Convert set back to list
unique_list = list(unique_numbers)
print("Unique List:", unique_list)

# Subset_ superset method

X = {1, 2}
Y = {1, 2, 3, 4}

print("Subset:", X.issubset(Y))
print("Superset:", Y.issuperset(X))

P = {1, 2}
Q = {3, 4}

print("Disjoint:", P.isdisjoint(Q))

# Remove all element/Clear the set
X.clear()
print("After clear():", X)