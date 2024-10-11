import StackFrontier
from maze_parser import readMaze
from nodeClasses import ActionNode
from reconstruct_path import reconstructPath


def dfs(adj):
    # Find the starting node
    startNode = list(filter(lambda a: a.isStart, adj))[0]

    if startNode is None:
        raise ValueError("Couldn't find starting node")
    
    print(f'Start node: {startNode.getNumber()}')
    
    # We need a stack frontier for this
    frontier = StackFrontier.StackFrontier()

    # A visited list
    visited = []

    frontier.push((startNode, None))

    # A variable with the parent
    parentNode = None

    # A list to keep track of all parents
    parents = []
    
    # Go through all nodes in the frontier
    while not frontier.isEmpty():
        currentNode = frontier.pop() # Get the current node

        # Add the neighbours of the current node
        for neigh in currentNode[0].getNeighbours():
            if neigh not in visited:
                frontier.push((neigh, currentNode[0].getNumber()))

        if currentNode[0] in visited: 
            continue # If already visited, skip

        visited.append(currentNode[0]) # Add it to the visited list

        # Search the parent with the same parent number for the current node in the
        # parents list
        parent = None
        parentResults = list(filter(lambda a: a.getNumber() == currentNode[1], parents))

        if len(parentResults) != 0:
            parent = parentResults[0]

        # Create the ActionNode
        actionNode = ActionNode(currentNode[0].getNumber(), parent, None)

        # Add the action node to the parents list
        parents.append(actionNode)

        #parentNode = actionNode # Switch the parent with the current

        if currentNode[0].isGoal:
            print(f'Found the goal in node {currentNode[0].getNumber()}')
            return actionNode
        
        

adj = readMaze('./maze1.txt', True)
lastNode = dfs(adj)

path = reconstructPath(lastNode)
print(path)
