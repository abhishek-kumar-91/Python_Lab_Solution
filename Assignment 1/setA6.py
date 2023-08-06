n = int(input("Enter the number"))
lastDigit = 0
firtDigit = 0

while n > 0:
    lastDigit = n % 10
    break

while n > 0:
    firtDigit = n % 10
    n //= 10
    

print(lastDigit+ firtDigit)