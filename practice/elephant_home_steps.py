# Elephant Home Steps
# Calculate steps for elephant to reach home
n = int(input("Enter number of steps: "))
steps = 0
position = 0
for i in range(n):
    direction = input(f"Step {i+1} - Enter direction (L/R): ").strip().upper()
    if direction == 'R':
        position += 1
    elif direction == 'L':
        position -= 1
print(f"Elephant is {abs(position)} steps away from home.")
