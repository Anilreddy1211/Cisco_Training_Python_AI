'''
Write a python program:
i. create an empty list
ii.display number of elements in the list # use len() function # -> 0
|
iii. use while loop - limit is 5
    a -> read a hostname from user input
    b -> append the hostname to the list
iv. display number of elements in the list # use len() function # ->5
|
v. use for loop - iterate through the list
|
vi. read a hostname from <STDIN>
vii. test input hostname is existing or not in the list
                             |                        |
viii.                        modify the hostname      |__add the hostname 
                                |__last Index 
                                
ix. display the list of hostnames - use for loop

'''
hosts=[]
print(f'length of the hosts list {len(hosts)}')
count = 0
while count < 5:
    h = input("Enter a hostname:")
    hosts.append(h) 
    count = count + 1

print(f"length of the hosts list:{len(hosts)}") 

for var in hosts:
    print(var) 
    

host_name  = input("Enter a hostname:")
if host_name in hosts:
    hosts[-1] = host_name 
else:
    hosts.append(host_name) 

print("\n") 
for i in hosts:
    print(i) 
    