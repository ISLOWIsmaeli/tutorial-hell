# # A string of characters that form a search pattern
import re
# # Search the string to see if it starts with "You" and ends with "Python"
# newTxt = "You can start learning Python"
# x = re.search("^You.*Python$",newTxt)

# if x:
#     print("Yes, we have a match!")
# else:
#     print("No match!")
# metacharacters,findall,search,sub,split
newTxt = "Python is very very easy to understand"
anotherTxt = "Python is very fun"

# x = re.findall("very",newTxt)
# print(x)
# x=re.search("\s",newTxt)
# y= re.search("rain",anotherTxt)
# print("First white space position: ",x.start())
# print(y)
# # split is used to return a list where the string has been split at each match
# splText= "Try to code with python"
# x=re.split("\s",splText,2)#separation process is done twice
# print(x)
#sub replaces one or many matches with a string
text="Python is very easy"
x=re.sub("\s","$",text,1)
print(x)