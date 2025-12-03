class Stack:
    def __init__(self):
        self.myStack = []
    
    def push(self, value):
        self.myStack.append(value)
    
    def pop(self):
        #if len(self.myStack) > 0:
        if not self.isEmpty():
            lastElem = self.myStack.pop()
            return lastElem
        else:
            return None # stack is empty
    
    def isEmpty(self):
        return len(self.myStack) == 0
    
    def peek(self):
        if self.isEmpty():
            return None # stack is empty
        return self.myStack[-1]
    
    def printStack(self):
        print(self.myStack)

if __name__ == "__main__":
    stack = Stack()
    stack.printStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.printStack()
    removedElem = stack.pop()
    stack.printStack()
    removedElem = stack.pop()
    stack.printStack()
    stack.push(40)
    stack.printStack()
    topElem = stack.peek()
    print(topElem)