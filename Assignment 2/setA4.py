class Stack:
    def __init__(self):
        self.stack =[]

    def size(self):
        print("Size of stack: ",len(self.stack))
        return len(self.stack)
    
    def isEmpty(self):
        print("Stack is Empty")
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stact.pop()
        else:
            print("Stack is Empty")
            return None
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def display(self):
        if not self.isEmpty():
            for i in range(self.size()):
                print(self.stack[i], end = " ")
        else:
            print("stack is Empty")
            return None
        


s = Stack()
s.isEmpty()
s.size()


s.push(5)
s.push(9)
s.push(10)
s.push(22)
s.push(33)
s.display()


