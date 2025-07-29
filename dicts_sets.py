
'''
employee_data = {
    "name": "John Doe",
    "employe_id": 12345,
    "salary": 75000,
    "department": "Engineering",
}
print(employee_data["employe_id"])
employee_data["salary"] = 80000
print(employee_data)
employee_data["email"] = "dfghjhgfdfghj@gamil.com"
print(employee_data)
employee_data.pop("employe_id")
print(employee_data) 
for key in employee_data:
    print(f"{key}: {employee_data[key]}")
for value in employee_data.values():
    print(value)
for key, value in employee_data.items():
    print(f"{key}: {value}")
    '''
    
ece_students_ids = {101, 102, 103, 104 , 103, 105}
print(ece_students_ids)
ece_students_ids.add(106)
print(ece_students_ids)

cs_students_ids = {201, 102, 203, 104, 205}
print(cs_students_ids.union(ece_students_ids))  # Union of two sets
print(cs_students_ids.intersection(ece_students_ids))  # Intersection of two sets
print(cs_students_ids.difference(ece_students_ids))  # Difference of two sets
print(cs_students_ids.symmetric_difference(ece_students_ids))  # Symmetric difference of two sets
ece_students_ids.discard(101)  
print(ece_students_ids)  # Discard an element 
ece_students_ids.discard(999)  # Discarding a non-existent element does not raise an error
print(ece_students_ids)