
n = int(input("Enter the number: "))
number = n
rev_num=0
ans = 0

while n > 0:
    digit = n % 10
    rev_num=rev_num*10+digit
    n //= 10

if number == rev_num:
    print("Palindrom number: ", rev_num)
else:
    print("Not a palindrom number: ", rev_num)
