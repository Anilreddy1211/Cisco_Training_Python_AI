# Using Function 

fobj = open('Day4/emp.csv', 'r')
L = fobj.readlines()
fobj.close()

total = 0

for var in L:
    if 'sales' in var:
        var = var.strip()
        emp_list = var.split(",")
        ecost = emp_list[-1]
        total = total + int(ecost)

print(f"Sum of sales dept emp's cost: {total}")

print("---------------------------------------------------using lambda--------------------------------------------------")

from functools import reduce

P1 = list(map(lambda a: a, open('Day4/emp.csv', 'r')))

P2 = list(filter(lambda a: 'sales' in a, P1))

P3 = list(map(lambda a: a.split(",")[-1], P2))

total = reduce(lambda a, b: int(a) + int(b), P3)

print(total)