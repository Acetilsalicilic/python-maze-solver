class QueueFrontier:
    def __init__(self):
        self.queue = []
    
    def any(self, node):
        return node in self.queue
    
    def pop(self):
        el = self.queue[0]
        self.queue = self.queue[1:]
        return el
    
    def push(self, node):
        self.queue.append(node)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False