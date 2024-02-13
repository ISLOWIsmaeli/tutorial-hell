#cannot duplicate, ordered
person = {
    "name":"fred",
    "age":30,
    "country": "Germany",
}
x = person["name"]
y= person.get("name")
k = person.keys()
v= person.values()
i= person.items()
if "name" in person:
    print("Yes,It's completed")
print(person)
print(i)
print(k)
print(y)
print(x)
print(v)

# print(len(person))
# print(type(person))