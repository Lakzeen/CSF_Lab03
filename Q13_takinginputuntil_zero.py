# Keep taking input until user enters 0
while True:
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        if number == 0:
            print("Exiting program...")
            break
        else:
            print(f"You entered: {number}")
    except ValueError:
        print("Please enter a valid number!")