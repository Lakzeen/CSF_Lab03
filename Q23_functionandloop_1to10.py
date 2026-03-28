def check_even_odd(num):
    """Check if a number is even or odd"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from user
n = int(input("Enter a number: "))

# Loop from 1 to n
print(f"\nNumbers from 1 to {n}:")
print("-" * 30)
for i in range(1, n + 1):
    result = check_even_odd(i)
    print(f"{i} is {result}")