java = int(input("Enter java marks "))
python = int(input("Enter python marks "))
cpp =  int(input("Enter cpp marks "))
c = int(input("Enter c marks "))
php = int(input("Enter php marks "))

avgMarks = (java  + python + cpp + c + php) / 6

if( avgMarks > 75):
    print("Distinction ", avgMarks)
elif(avgMarks >= 60 and avgMarks < 75):
    print("First class ", avgMarks)
elif(avgMarks >= 50 and avgMarks < 60):
    print("Second Class ", avgMarks)
elif(avgMarks >= 35):
    print("Pass ", avgMarks)
else:
    print("fail ", avgMarks)

