#binary to decimal function

# def binaryToDecimal(binary):
 
#     decimal, i = 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     print(decimal)

# binaryInput = int(input("Enter the binary number: "))
# binaryToDecimal(binaryInput)

#decimal to binary function

def decimalToBinary(n):
 
    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)
 
     
    print(n%2, end=' ')

decimalInput = int(input("Enter the decimal number: "))
decimalToBinary(decimalInput)