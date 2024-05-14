#geeksforgeeks
#Implement Queue using array
class MyQueue :
    def __init__(self) -> None:
        self.queue = []
        self.rear = 0
        self.front = 0
        pass
    
    def push(self,x):
        self.queue.append(x)
        self.rear += 1

    def pop(self):
        y = self.front
        self.front += 1
        return self.queue[y]
