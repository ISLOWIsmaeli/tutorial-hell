class Player:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname

        pass
class NewPlayer(Player):
    def __init__(self,fname,lname,total):
        Player.__init__(self, fname,lname)
        self.total =total

    def getDetails(self):
        return "%s %s has spent %s in total" % (self.fname, self.lname, self.total)
        
newP = NewPlayer("Ismael", "lennox", 494949)

print(newP.getDetails())