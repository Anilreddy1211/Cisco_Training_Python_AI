port = int(input("Enter port number: "))

if 5001 <= port <= 5999:
    app_name = "Flask"
else:
    app_name = "WebApp"

print(f"App Name is: {app_name}")
print(f"Running Port Number is: {port}")

app_name = input("Enter app name: ")

if app_name in "crm application running in flask web app":
    port = 5000
else:
    port = 8080

print(f"App Name is: {app_name}")
print(f"Running Port Number is: {port}")