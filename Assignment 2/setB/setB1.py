userString = input("Enter string: ")
newString = ""

if len(userString) < 2:
    print("Empty string ")
else:
    newString = userString[:2]+userString[len(userString)-2:]


print(userString)
print(newString)
    