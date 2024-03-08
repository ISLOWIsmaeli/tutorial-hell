import collections
player=collections.namedtuple("player",["name","age","team"])
p1=player("Ian",44,"Kenya")
print(p1.name,p1.age,p1.team,sep=",,")