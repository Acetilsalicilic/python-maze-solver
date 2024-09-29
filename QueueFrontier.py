class QueueFrontier:
    def __init__(self):
        self.queue = []
    
    def any(self, node):
        return node in self.queue
    
    def pop(self):
        el = self.queue[0]
        self.queue.remove(0)
        return el
    
    def push(self, node):
        self.queue.append(node)