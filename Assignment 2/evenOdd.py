a = int(input("enter number: "))



if(a > 0 and a % 2 == 0):
    print(f"Even number: {a}")
elif(a > 0 and a % 2 != 0):
    print(f"Odd number: {a}")
else:
    print("Number is negative or less than 1: {a}")