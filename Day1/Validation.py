correct_username = "admin"
count = 0

while count < 3:
    username = input("Enter username: ")
    count += 1

    if username == correct_username:
        print(f"Username is Valid - attempt: {count}")
        break

    print(f"Attempts left: {3 - count} of 3")

else:
    print("Account is blocked")