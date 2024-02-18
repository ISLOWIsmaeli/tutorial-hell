#self is a reference to the current instance of the class
class Person:
    """create a new Person"""
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname

newPerson = Person("Ismael","Lennox")
anotherOne = Person("Sylus","Ojore")

newPerson.fname = "Cris"

print(newPerson)
print(newPerson.fname)
print(newPerson.lname)
print(anotherOne)
print(anotherOne.fname)

del newPerson.fname #deleted the property hence cannot be accessed
del newPerson #deleted the whole object
print(newPerson.fname)