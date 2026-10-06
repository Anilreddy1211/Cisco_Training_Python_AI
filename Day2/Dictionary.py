hosts = {}

print(f"Number of elements in the dictionary: {len(hosts)}")

count = 0

while count < 5:
    h = input("Enter a hostname: ")
    ip = input("Enter an IP address: ")

    hosts[h] = ip
    count += 1

print(f"Number of elements in the dictionary: {len(hosts)}")

# Display dictionary
for var in hosts:
    print(f"Hostname: {var}\tIP Address: {hosts[var]}")

# 1.Update or add hostname
h = input("Enter a hostname to update: ")

if h in hosts:
    hosts[h] = "127.0.0.1"
    print("IP address updated.")
else:
    print(f"Sorry, hostname {h} does not exist.")
    hosts[h] = "127.0.0.1"
    print("Hostname added.")

# Display updated dictionary
for var in hosts:
    print(f"Hostname: {var}\tIP Address: {hosts[var]}")
    
''' setdefault()
              |
              |__`setdefault()` adds a new key to the dictionary only when the key is not already present.
              
    get() – Gets the value of a key from the dictionary.
    update() – Adds new key-value pairs or updates existing ones.
    keys() – Returns all the keys in the dictionary.
    values() – Returns all the values in the dictionary.
    items() – Returns all key-value pairs in the dictionary.
    pop() – Removes a specific key and its value from the dictionary.
    popitem() – Removes the last key-value pair from the dictionary.
    clear() – Removes all key-value pairs from the dictionary.
    copy() – Creates a copy of the dictionary. 
'''


