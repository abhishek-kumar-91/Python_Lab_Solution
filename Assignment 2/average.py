print("Average of n number")

n = int(input("Enter n number:"))
result = 0
finalAns = 0

for i in range(n):
    a = int(input("enter a number: "))
    result += a
    

finalAns=result/n

print(result)

print(finalAns)