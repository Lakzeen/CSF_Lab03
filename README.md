# CSF_Lab03
## AIM
To develop a clear understanding of control structures in Python by implementing conditional statements, loops, break and continue statements, and to learn how to define and invoke functions for solving programming problems in a structured and efficient manner.
## Programs and Explanation
1. Checking if the number is positive or not: In this program we check if a number is positive or negative by assigning a variable.Conditions such as variable>0 is given as positive and add else to print negative.
#
2. Even and Odd number: To check if the entered number is even or odd, assign a variable. Then create a condition where the number entered is divisible by 2 and put "else" for odd.
#
3. Largest number: This program compares two numbers entered by the user:

Input: It prompts the user to enter two integers (num1 and num2)

Conversion: int() converts the input strings to integers

Comparison: The if statement checks if num1 is greater than num2

If true → prints "The first number is greater."

If false → prints "The second number is greater."
#
4. Largest of three numbers: Input: Takes three integers (a, b, c) from the user

Comparison: Checks which one is biggest

First checks if a is greater than both b AND c → prints "a is the largest"

If not, checks if b is greater than both a AND c → prints "b is the largest"

If neither is true, prints "c is the largest"
#
5. Marks Grading: Input: Takes marks as a decimal number (float)

Grading logic:

80 or above → Grade A

60 to 79 → Grade B

40 to 59 → Grade C

Below 40 → Fail

 The if-elif-else structure checks conditions in order. Once a condition is met, it prints the grade and skips the rest.
 #
 6.Addition,subtraction,multiplication and division:
Infinite loop (while True) - keeps repeating forever

Takes two numbers from the user

Shows a menu with 4 operations:

1 = Addition 

2 = Subtraction 

3 = Multiplication 

4 = Division 

Performs the chosen operation and displays the result

Invalid choices show an error message

Repeats automatically
#
7. 1 to 10 using loop:range(1, 11) generates numbers starting from 1 up to but not including 11 → so 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

The for loop goes through each number

print(x) displays each number on a new line
#
8. Loop for even number: range(1, 21) generates numbers 1 through 20

x % 2 == 0 checks if a number is even (divisible by 2 with no remainder)

Only numbers that satisfy this condition get printed
#
9. Sum of 10 natural numbers:This program calculates the sum of the first 10 natural numbers (1 through 10):

How it works:

sum = 0 → starts with zero

i = 1 → starts counting from 1

While loop runs as long as i <= 10:

Adds current i to sum

Increases i by 1 for the next iteration

After the loop finishes, prints the total
#
10. Multiplication table:This program prints the multiplication table for a given number:

How it works:

Takes a number from the user

range(1, 11) generates multipliers from 1 to 10

The for loop goes through each multiplier

Uses .format() to display the multiplication in a neat table format
#
11. Number 1 to 5 using while loop:This program prints numbers 1 through 5 using a while loop:

How it works:

i = 1 → initializes the counter starting at 1

while i <= 5: → continues looping as long as i is less than or equal to 5

print(i) → displays the current value of i

i = i + 1 → increments i by 1 for the next iteration
#
12. Finding sum using while loop:This program calculates the sum from 1 up to a given number:

How it works:

sum = 0 → starts with zero

i = 1 → starts counting from 1

While loop runs as long as i is less than or equal to num (user input)

Adds current i to sum each iteration

Increments i by 1

Prints the total after the loop ends
#
13. Taking input until it is zero:This program continuously asks for numbers until the user enters 0:

How it works:

Infinite loop (while True) keeps running until broken

Takes user input as a string

Try-except block handles errors gracefully:

Try: Converts input to integer

If number == 0 → prints exit message and breaks the loop

Otherwise → displays the number entered

Except: Catches ValueError if input is not a valid number → shows error message
#
14. Breaking loop at 6:This program prints numbers 1 through 5 and stops when it reaches 6:

How it works:

range(1, 11) generates numbers 1 to 10

The for loop goes through each number

if i == 6: checks if the current number is 6

break → immediately exits the loop when i equals 6

print(i) only executes for numbers before the break
#
15. Continue at number 5:This program prints numbers 1 through 10, except 5:

How it works:

range(1, 11) generates numbers 1 to 10

The for loop goes through each number

if i == 5: checks if the current number is 5

continue → skips the rest of the loop for that iteration and moves to the next number

print(i) executes for all numbers except when i == 5
#
16. Searching a number:This program searches for a number in a list and stops when found:

How it works:

numbers = [2, 4, 6, 8, 10] → the list to search

search_num = 8 → the target number

The for loop goes through each number in order

if num == search_num: → checks if current number matches

When found → prints success message and breaks out of the loop

print(f"Checking {num}...") → shows each number being checked
#
17. Helloworld:This program defines and calls a function that prints a greeting:

How it works:

def greet(): → defines a function named greet

print("Hello, World!") → the function's action (prints the message)

greet() → calls the function, making it execute
#
18. Square of numbers:This program calculates the square of a number with error handling:

How it works:

def square(n): → defines a function that takes a number and returns its square (n * n)

Try block:

Takes user input and converts to integer

Calls the square() function to calculate the square

Displays the result

Except block:

Catches ValueError if user enters non-numeric input

Shows an error message without crashing
#
19. Adding numbers:This program takes two numbers and displays their sum:

How it works:

Takes first number as integer → num1

Takes second number as integer → num2

Adds them together → sum = num1 + num2

Prints the result using an f-string
#
20. Even and odd: This program checks whether a number is even or odd:

How it works:

Takes an integer input from the user → x

x % 2 == 0 → checks if the remainder when divided by 2 is zero

If true → number is even → prints "The number is even."

If false → number is odd → prints "The number is odd."
#
21. Factorial:This program calculates the factorial of a given number:

How it works:

Takes an integer input → num

Initializes fact = 1 (starting value for multiplication)

For loop runs from 1 to num:

fact = fact * i → multiplies current factorial value by each number

Prints the final result
#
22. Print multiplication table:This program prints the multiplication table for a given number:

How it works:

Takes a number from the user → number

range(1, 11) generates multipliers from 1 to 10

The for loop goes through each multiplier

Uses .format() to display the multiplication in a formatted table
#
23. Function and loop:

 This program checks whether numbers from 1 to n are even or odd:

How it works:

Function definition:

def check_even_odd(num): → defines a function that takes a number

Returns "Even" if number is divisible by 2, otherwise "Odd"

User input:

Takes a number n from the user

Loop and display:

Loops from 1 to n

Calls check_even_odd(i) for each number

Prints whether each number is even or odd
#
24. Menudriven calculator:This program creates a calculator with an exit option that runs until the user chooses to quit:

How it works:

Infinite loop (while True) continues until broken

Takes two numbers from the user

Displays a menu with 5 options:

1 = Addition

2 = Subtraction

3 = Multiplication

4 = Division

5 = Exit

Performs the chosen operation and displays the result






