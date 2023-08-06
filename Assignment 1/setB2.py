def binary_to_decimal(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num


binary_input = input("Enter the binary number: ")
binary_to_decimal(binary_input)