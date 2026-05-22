# Odd Numbers in a Range
start = int(input("Enter start: "))
end = int(input("Enter end: "))
print(f"Odd numbers between {start} and {end}:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()
