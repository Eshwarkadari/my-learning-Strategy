# Watermelon Equal Weight
# Can a watermelon of given weight be split into two equal even parts?
w = int(input("Enter watermelon weight: "))
if w > 2 and w % 2 == 0:
    print("YES - Can be split into two equal even parts!")
else:
    print("NO - Cannot be split equally.")
