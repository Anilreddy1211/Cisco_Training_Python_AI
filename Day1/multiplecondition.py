dbName = input("Enter database name: ")

if dbName == "mysql":
    port = 3306
elif dbName == "postgresql":
    port = 5432
elif dbName == "mongodb":
    port = 27017
else:
    dbName = "defaultDB"
    port = 8000

print(f"Database Name is: {dbName}")
print(f"Running Port Number is: {port}")