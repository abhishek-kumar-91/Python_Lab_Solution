#abc,xyz  xycabz

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

newStr = str2[:2]+str1[2:]+str1[:2]+str2[2:]


print("Original string: ",str1,str2)
print(newStr)
