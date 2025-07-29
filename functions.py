
def calculate_interest(principle , rate, time): 
return(principle * rate * time) / 100

principal = 10000
rate = 5
time = 2
calculated_amount = calculate_interest(principal, rate, time)
print(calculated_amount)


def check_even_or_odd(i):
    if i%2==0:
        print("even number")
    else:
        print("odd number")
    
check_even_or_odd(12)

def display_student_info(name, roll_no, branch="ECE"):
    """Displays student information with a default branch."""
    print(f"Student: {name}, Roll No: {roll_no}, Branch: {branch}")

# Call the function with default branch
display_student_info("Your Name", 213456)

# Call the function with a different branch using keyword argument
display_student_info(roll_no=987654, name="Another Student", branch="CSE")

print("Hello", "World!")           # Output: Hello World!
print("Hello", "World!", sep="---") # Output: Hello---World!
print("Line 1", end=" ")           # Prints "Line 1 " (no newline)
print("Line 2")                    # Prints "Line 2" on the same line as "Line 1"
# Output: Line 1 Line 2

# Formatting with f-strings (introduced earlier, but reiterating importance)
item = "Laptop"
cost = 1200.50
print(f"The {item} costs ${cost:.2f}.") # Output: The Laptop costs $1200.50.

try:
    user_num_str = input("Please enter an integer: ")
    user_num = int(user_num_str) # This might raise a ValueError
    print(f"You entered: {user_num}")
except ValueError:
    print("Invalid input! That was not a valid integer. Please try again.")
print("Program continues here.") # This line will run even if an error occurred and was handled.
