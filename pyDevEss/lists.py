fruits = ["fig","banana","lemon","fig"]
numbers = [1,2,3]
newFruits = ["Watermelon","Cherry"]
print(fruits)
fruits[0:2] = ["Orange","lemon"]
print(fruits)
fruits.insert(1,"fig")
print(fruits)
fruits.extend(newFruits)
print(fruits)