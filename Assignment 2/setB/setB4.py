class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        print("Queue is Empty")
        return len(self.queue) == 0
    
    def size(self):
        if not self.isEmpty():
            return len(self.queue)
        else:
            print("Queue is Empty")

    def push(self,item):
        self.queue.append(item)

    def pop(self):
        if not self.isEmpty():
            list.reverse(self.queue)
            return self.queue.pop()
        
    def peek(self):
        if not self.isEmpty():
            list.reverse(self.queue)
            return self.queue(-1)
    
    def display(self):
        if not self.isEmpty():
            list.reverse(self.queue)
            for i in range(self.size()):
                print(self.queue[i], end = " ")


q = Queue()
q.push(5)
q.push(4)
q.push(9)
q.push(66)
q.push(3)

print(q.pop())
q.display()
