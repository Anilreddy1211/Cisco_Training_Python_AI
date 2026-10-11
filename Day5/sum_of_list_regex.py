
'''
S = ['120GB','500GB','GB200','150Gb','300gb','400']

Calculate sum of the size - display total size
'''
import re
S = ['120GB','500GB','GB200','150Gb','300gb','400']

total = 0
for var in S:
    size = re.sub('[A-Za-z]','',var)
    total = total + int(size)

print(f' Sum of {S} disk size is:{total} GB\n')

print([re.sub('[A-Za-z]','',var) for var in S])