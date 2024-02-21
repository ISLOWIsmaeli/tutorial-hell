import os
os.chdir("c:\\Users\\Lennox\\Documents\\myProjects\\tutorials\\tutorial-hell\\pyDevEss")
file = open("main.txt","r")
print(file.read(20))
file.close()
print(file.readline())
print(file.readline())

for x in file:
    print(x)