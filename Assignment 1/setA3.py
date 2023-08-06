number = int(input("Enter the number: "))
ans = 0

for i in range(1, number):
    if(number % i == 0 and number != i):
        ans += i



print(ans)