a  = int(input("enter a value: "))
b = int(input("enter b value: "))
c = int(input("enter c value: "))


# maxAns = max(a,b,c)

# print(f"Max number is: {maxAns}")

maxStore = 0

if(a > b and a > c):
    maxStore = a
elif(b > a and b > c):
    maxStore = b
else:
    maxStore = c

print("Max number is: ", maxStore)
