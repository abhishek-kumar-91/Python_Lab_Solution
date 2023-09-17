stringEnter = input("Enter string")

firstCharacter =stringEnter[0]

newString=firstCharacter+stringEnter[1:].replace(firstCharacter,'$')


print("Original String: ", stringEnter)
print("With changes occured: ", newString)
