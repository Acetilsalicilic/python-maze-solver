class StackFrontier:
    def __init__(self):
        self.stack = []
    
    def any(self, node):
        return node in self.stack
    
    def push(self, node):
        self.stack.append(node)
    
    def pop(self):
        return self.stack.pop()
    
    def getCount(self):
        return len(self.stack)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False