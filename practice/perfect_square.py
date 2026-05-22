# Perfect Square Checker
import math
num = int(input("Enter a number: "))
sqrt = int(math.sqrt(num))
if sqrt * sqrt == num:
    print(f"{num} is a Perfect Square! ({sqrt} x {sqrt})")
else:
    print(f"{num} is NOT a Perfect Square.")
