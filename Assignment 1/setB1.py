n = int(input("Enter the number: "))
evenAns = 0
oddAns = 0
zeroAns = 0

while n > 0:
    digit = n % 10

    if(digit == 0):
        zeroAns += 1
    elif(digit % 2 == 0):
        evenAns += 1
    elif(digit % 2 != 0):
        oddAns += 1
        
    n //= 10


print(zeroAns)
print(evenAns)
print(oddAns)

