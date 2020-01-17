str = "What is this ?" #initial string
reversedString=[]
index = len(str) # calculate len of string and save in index
while index > 0:
    reversedString += str[ index - 1 ] # save the value of str[index-1]
    index = index - 1 # decrement index
print(reversedString) # reversed string
