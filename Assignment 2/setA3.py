

def removeOddString(inputString):
    result = ""
    
    for i in range(len(inputString)):
        if i % 2 != 0:
            result += inputString[i]

    return result


s = input("Enter string ")

r = removeOddString(s)
print("Original String: ", s)
print("Remove String: ", r)
