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

    frontier.push(startNode)

    # A variable with the parent
    parentNode = None
    
    # Go through all nodes in the frontier
    while not frontier.isEmpty():
        currentNode = frontier.pop() # Get the current node

        # Add the neighbours of the current node
        for neigh in currentNode.getNeighbours():
            if neigh not in visited:
                frontier.push(neigh)

        if currentNode in visited: 
            continue # If already visited, skip

        visited.append(currentNode) # Add it to the visited list

        # Create the ActionNode
        actionNode = ActionNode(currentNode.getNumber(), parentNode, None)
        parentNode = actionNode # Switch the parent with the current

        if currentNode.isGoal:
            print(f'Found the goal in node {currentNode.getNumber()}')
            return actionNode
        
        

adj = readMaze('./maze2.txt', True)
lastNode = dfs(adj)

path = reconstructPath(lastNode)
print(path)