#come up with a 3 by 4 matrix
#eliminate using gausss jordan
#produce the answer
# def find_smallest(x,y,z):
#     smallest=x
#     if y < smallest:
#         smallest =y
#     if z < smallest:
#         smallest=z
#     return smallest

trial=[[2,1,2,8],[1,-3,3,-4],[4,2,-1,1]]
minimum_value=float('inf')
minimum_index=0
# print("Please enter a 3 by 4 variable simultaneous equation matrix")
# for i in range(0,3,1):
#     for j in range(0,4,1):
#         print("Enter row[",(i+1),"] columnt[",(j+1),"]",sep="")
#         trial[i][j]=int(input())
#         print(trial[i][j])
for i in range(len(trial)):
    if trial[i][0]<minimum_value:
        minimum_value=trial[i][0]
        minimum_index=i
trial[0],trial[minimum_index]=trial[minimum_index],trial[0]
print(trial)


