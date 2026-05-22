my_cources=["vlsi","design","python","java","cpp"]
print(my_cources)
print(my_cources[0])
print(my_cources[-1])
my_cources[2]= "emberred"
print(my_cources)
my_cources.append("eng")
print(my_cources)
my_cources.insert(0,"math")
print(my_cources)
my_cources.remove("vlsi")
print(my_cources)
my_cources.pop(-1)
print(my_cources)
for index, cources in enumerate(my_cources):
    print(f"{index}: {cources}")
print(len(my_cources))
