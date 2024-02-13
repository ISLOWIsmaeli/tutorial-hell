#cannot duplicate, ordered, changeable
person = {
    "name":"fred",
    "age":30,
    "country": "Germany",
}

person["age"] = 40
person.update({"age":30})
person.update({"id":21,"number":50})

print(person)
# x = person["name"]
# y= person.get("name")
# k = person.keys()
# v= person.values()
# i= person.items()
# if "name" in person:
#     print("Yes,It's completed")
# print(person)
# print(i)
# print(k)
# print(y)
# print(x)
# print(v)

# print(len(person))
# print(type(person))