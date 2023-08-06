number = int(input("Enter number"))
n = number
ans = 0

while n > 0:
    digit = n % 10
    ans += digit * digit * digit
    n //= 10
   
if ans == number:
    print("Armstrong number is: ", ans)
else:
    print("Not a armstrong number: ", ans)
