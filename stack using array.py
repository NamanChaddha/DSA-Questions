class myStack:
    def __init__(self,n):
        self.s = [0] *n
        self.capacity =n
        self.topIndex = -1
    def push(self, x):
        if self.isFull():
            return 1==0
        self.topIndex+=1
        self.s[self.topIndex]=x
        return 1==1

    def pop(self):
        if self.isEmpty():
            return -1
        x=self.s[self.topIndex]
        self.topIndex-=1
        return x

    def isFull(self):
        if self.topIndex == self.capacity - 1:
            return 1==1
        return 1==0

    def isEmpty(self):
        if self.topIndex==-1:
            return 1==1
        return 1==0

    
    def peek(self):
        # Returns the top element of the stack
        if self.isEmpty():
            return -1
        return self.s[self.topIndex]
