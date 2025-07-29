try:
    with open("my_notes.txt", "w") as f:
        f.write("my names is Eshwar\n")
        f.write("my roll number is 456543\n")
        f.write("my branch is ECE\n")
        f.write("learning python is fun!\n")
except FileNotFoundError:
    print("Error: my_notes.txt not found.")
except IOError as e:
    print(f"Error writing to file: {e}")

try:
    with open("my_notes.txt", "a") as f:
        f.write("I am in third year.\n")
        f.write("I love coding.\n")
        for i in range(5):
            if i % 2 == 0:
                line_to_write = f"This is an even line: {i+1}\n" # Prepare the string
                f.write(line_to_write) # Write to the file
                print(f"Wrote: {line_to_write.strip()} to my_notes.txt") # Print to console for feedback
            else:
                print(f"Skipping line {i+1} (not writing to file)") # Print to console for feedback
        print("Content appended to my_notes.txt.")
        
except FileNotFoundError:
    print("Error: my_notes.txt not found.")
except IOError as e:
    print(f"Error appending to file: {e}")
    
try:
    file = open("my_notes.txt", "r")
    for line in file:
        print(line.strip())  # Print each 
        print("File read successfully.")
        
except FileNotFoundError:
    print("Error: my_notes.txt not found.")
except IOError as e:
    print(f"Error reading file: {e}")
    
try:
    file = open("my_not.txt", "r")
    for line in file:
        print(line.strip())  # Print each line without extra whitespace
        print("File read successfully.")
        
except FileNotFoundError:
    print("Error: my_notes.txt not found.")
except IOError as e:
    print(f"Error reading file: {e}")