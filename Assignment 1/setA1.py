n = int(input("Enter the length of the number "))
sumAns = 0

while n > 0:
    digit = n % 10
    sumAns += digit
    n//=10

print(sumAns)



    
