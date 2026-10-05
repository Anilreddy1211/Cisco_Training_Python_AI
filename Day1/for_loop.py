s = '123456789'
total = 0

for var in s:
    total = total + int(var)

print(f"Sum of the digits in string s is: {total}")




s = "python programming"
count = 0

for var in s:
    if var in "aeiou":
        count = count + 1

print(f"Number of vowels in string s is: {count}")