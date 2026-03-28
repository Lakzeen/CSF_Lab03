def square(num):
    return num ** 2

try:
    number = int(input("Enter a number: "))
    result = square(number)
    print(f"The square of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")  