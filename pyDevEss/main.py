import newModule as any
import platform
from newModule import player

any.new("Ismael")
x=any.player["name"]
y=any.player["age"]
print(x,y)

op =dir(platform)
print(op) #prints all functions within a given module
print(help('modules'))