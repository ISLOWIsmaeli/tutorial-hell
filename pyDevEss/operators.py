#identity and members operators (is and is not)
#membership if a sequence is present in an object
list1=["fig","apple"]
list2=["fig","apple"]
list3 = list2

# print(list1 is list2) # 2 different locations in memory
# print(list3 is list2) # point to same memory
# print(list1 is not list2)

print("fig" in list1)
print("sweet" not in list1)