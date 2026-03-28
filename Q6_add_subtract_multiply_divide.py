while True:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("The sum is: ", num1+num2)
    elif choice==2:
        print("The difference is: ", num1-num2)
    elif choice==3:
        print("The product is: ", num1*num2)
    elif choice==4:
        print("The quotient is: ", num1/num2)
    else:
        print("Invalid choice.")