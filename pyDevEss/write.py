import os
os.chdir("c:\\Users\\Lennox\\Documents\\myProjects\\tutorials\\tutorial-hell\\pyDevEss")
# file = open("write.txt","a")#add content
file = open("write.txt","a") # overwrite content
file.write("Writing new  to this text file")
file.close()