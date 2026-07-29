class SpecialStack:

    def __init__(self):
        # Define Stack
        self.st=[]
        self.minele=99999
    
    def push(self, x):
        # Add an element to the top of Stack
        if x>self.minele:
            self.st.append(x)
        else:
            self.st.append(2*x-self.minele)
            self.minele=x
            
    
    def pop(self):
        # Remove the top element from the Stack
        if self.st[-1]>=self.minele:
            self.st.pop()
        else:
            self.minele=2*self.minele-self.st[-1]
            self.st.pop()
    
    def peek(self):
        # Returns top element of Stack
        if self.st==[]:
            return -1
        if self.st[-1]>=self.minele:
            return self.st[-1]
        else:
            return self.minele
        
    def isEmpty(self):
        # Check if the stack is empty
        if self.st:
            return False
        return True
    
    def getMin(self):
        # Finds minimum element of Stack
        if self.st==[]:
            return -1
        return self.minele
