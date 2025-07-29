'''
marks = 25
if marks >=50:
    print("You have passed the exam.")
    
year= int(input("Enter the year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("You got an A grade.")
elif percentage >= 80:
    print("You got a B grade.")
elif percentage >= 70:
    print("You got a C grade.")
elif percentage >= 60:
    print("You got a D grade.")
else:
    print("You got an F grade.")
'''
for char in "eshwar":
    print(char)