n = int(input("Enter count of digit"))
l = []

for i in range(n):
      x= int(input(f"Enter {i} value: "))
      l.insert(i,x) 
      
list.sort(l)

for i in range(n-1):
      if l[i] == l[i+1]:
            print("duplicate")
            break
      else:
            print("Unique")
            break
            
        