import time

def pin_test():
    correct_pin = "1234"
    max_attempts = 3
    attempt = 0

    with open("pin_history.log", "a") as f:

        while attempt < max_attempts:

            user_pin = input("Enter ATM PIN: ")

            if user_pin == correct_pin:
                attempt += 1

                f.write(
                    f"Success - {attempt} - {time.ctime()}\n"
                )

                print("Valid PIN")
                print("PIN validation successful")
                break

            else:
                attempt += 1

                f.write(
                    f"Invalid PIN - {user_pin} - {time.ctime()}\n"
                )

                print("Invalid PIN")
                print(f"Attempts remaining: {max_attempts - attempt}")

        if attempt == max_attempts and user_pin != correct_pin:
            f.write(f"PIN Blocked - {time.ctime()}\n")
            print("ATM PIN is blocked")


pin_test()