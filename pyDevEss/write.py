import os
os.chdir("c:\\Users\\Lennox\\Documents\\myProjects\\tutorials\\tutorial-hell\\pyDevEss")
# file = open("write.txt","a")#add content
file = open("write.txt","w") # overwrite content
file.write("Writing new  to this text file")
file.close()

file = open("demo.txt","x")