'''

for i in range (1,11):
    print(sum(range(i+1)))
    
count = 6
while count > 0:
    count -= 1
    print(count)
print("Blast off!") 



for i in range(1, 10):
    if i == 15:
        print(" we found the target 5")
        break 
    else:
        print("Not found yet, keep looking...")
print("Loop ended by break.")



for i in range(1, 11):
    if i % 2 != 0: 
        continue   
    print(f"{i} is an even number.")
    
'''

cars = ["Ford", "Volvo", "BMW"]
for car in cars:
    print(car)

# Or with index
for index, car in enumerate(cars):
    print(f"{index}: {car}")