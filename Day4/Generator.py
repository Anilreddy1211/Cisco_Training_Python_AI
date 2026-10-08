'''Generator
A generator is a special type of iterator that produces values one at a time instead of storing all values in memory at once.'''
def square(n):
    for i in range(1, n + 1):
        yield i * i

x = square(5)

for value in x:
    print(value)