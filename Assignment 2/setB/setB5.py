userStr = input("Enter string ")

res = {}

for i in userStr:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for char,count in res.items():
    if count> 1:
        print(f"{char} {count}")




print("User given string: ", userStr)
