
# Example 1: Raising a built-in exception

try:
    n = input("Enter n Value: ")

    if int(n) > 100:
        raise ValueError("n value is above 100")

    print("Valid n value:", int(n))

except Exception as e:
    print("Error:", e)


# Example 2: Creating a custom exception

class InsufficientBalanceError(Exception):
    pass


balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)
