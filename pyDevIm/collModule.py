import collections
player=collections.namedtuple("player",["name","age","team"])#it required a field name
p1=player("Ian",44,"Kenya")
print(p1.name,p1.age,p1.team,sep=",,")
#ordered dict remembers the order of the keys by the time they were first inserted
d1=collections.OrderedDict()
d1["First: "]=35
d1["Second: "]=40
d1["Third: "]=45
d1["Fourth: "]=50
for k,v in d1.items():
    print(k,v)