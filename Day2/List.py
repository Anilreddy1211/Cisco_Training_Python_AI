
# LIST
#======================================
''' A list is an ordered and mutable collection in Python that can store multiple values, including duplicate and different data types.'''

# 1. Create a List
numbers = [10, 20, 30, 40, 20]

print("List:", numbers)

# 2. Length
print("Length:", len(numbers))

# 3. Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 4. Slicing
print("Slice:", numbers[1:4])

# 5. Membership
print("20 in list:", 20 in numbers)
print("50 not in list:", 50 not in numbers)

# 6. Add one element
numbers.append(50)
print("After append:", numbers)

# 7. Add element at specific position
numbers.insert(1, 15)
print("After insert:", numbers)

# 8. Add multiple elements
numbers.extend([60, 70])
print("After extend:", numbers)

# 9. Update element
numbers[0] = 100
print("After update:", numbers)

# 10. Count an element
print("Count of 20:", numbers.count(20))

# 11. Find index
print("Index of 30:", numbers.index(30))

# 12. Remove specific value
numbers.remove(20)
print("After remove:", numbers)

# 13. Remove last element
numbers.pop()
print("After pop:", numbers)

# 14. Sort the list
numbers.sort()
print("After sort:", numbers)

# 15. Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# 16. Loop through list
print("List elements:")
for value in numbers:
    print(value)

# 17. Copy the list
new_list = numbers.copy()
print("Copied list:", new_list)

# 18. Clear the list
numbers.clear()
print("After clear:", numbers)