import random
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
        
def max_find(arr):
    if not arr:
        return None
    max_val = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            max_val = arr[i]
    return max_val

def min_find(arr):
    if not arr:
        return None
    min_val = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min_val:
            min_val = arr[i]
    return min_val

student_score = [random.randint(50,100) for _ in range(15)]
print("student_scores", student_score)

try:
    target_score = input("enter your target score:")
    target_sc= int(target_score)
    
    index =linear_search(student_score,target_sc)
    
    if index != -1:
        print(f"target{target_sc} found at {index} ")
    else:
        print("target is not found")
except IOError as e:
    print("error while entering")
max_score = max_find(student_score)
min_score = min_find(student_score)

print(f"max_student score:{max_score}" )
print(f"min student score{min_score}")