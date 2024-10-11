from QueueFrontier import QueueFrontier
from maze_parser import readMaze
from nodeClasses import ActionNode
from reconstruct_path import reconstructPath


def bfs(adj):
    # Same steps as DFS
    startNode = list(filter(lambda a: a.isStart, adj))[0]

    if startNode is None:
        raise ValueError("Couldn't find starting node")
    
    # Now, a queue frontier
    frontier = QueueFrontier()

    # The visited list
    visited = []

    # Parent variable
    parentNode = None

    # Add teh first node to the frontier
    frontier.push(startNode)

    # The BFS itself:
    while not frontier.isEmpty():
        currentNode = frontier.pop() # Get the current node

        # Add the neighbours of the current node to the frontier
        for neigh in currentNode.getNeighbours():
            if neigh not in visited:
                frontier.push(neigh)
        
        if currentNode in visited:
            continue # Not needed i think, but whatever

        visited.append(currentNode) # We are visiting the current node, so let's add it

        # Create the ActionNode
        actionNode = ActionNode(currentNode.getNumber(), parentNode, None)
        parentNode = actionNode # Switch the parent node with the current

        if currentNode.isGoal:
            print(f'Found the goal in node {currentNode.getNumber()}')
            return actionNode
        # Das end

adj = readMaze('./maze3.txt', True)
lastNode = bfs(adj)

if (lastNode is None):
    raise ValueError("lastNode is NONE")

path = reconstructPath(lastNode)
print(path)