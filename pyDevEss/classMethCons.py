class Person:
    """create a new Person"""
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname
    def new(self):
        print("Hi, my nae is" + self.fname)
        print("Hi, my name is " + self.lname)


newPerson = Person("Dony","Beckar")
anotherOne = Person("first","last")