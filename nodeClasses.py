class ActionNode:
    def __init__(self, number, parent, action, isGoal = False, isStart = False):
        self.number = number
        self.parent = parent
        self.action = action
        self.isGoal = isGoal
        self.isStart = isStart
    
    def getParent(self):
        return self.parent
    
    def getNumber(self):
        return self.number

class GraphNode:
    def __init__(self, number, isGoal = False, isStart = False):
        if (isGoal and isStart):
            raise ValueError("GraphNode can't be goal and start at the same time!")
        self.number = number
        self.isGoal = isGoal
        self.isStart = isStart

        # Neighbours init
        self.neighbours = []

    def getNumber(self):
        return self.number
    """     
    def getParent(self):
        return self.parent
    
    def getAction(self):
        return self.action """
    
    def pushNeighbour(self, node):
        self.neighbours.append(node)

    def getNeighbours(self):
        return self.neighbours
