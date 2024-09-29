from nodeClasses import GraphNode
from printAdjacency import printAdjacency

def readMaze(file, printMatrix = False):
    avMoves = [ # (vertical, horizontal)
        (0, 1), # Move to the right
        (0, -1), # Move to the left
        (1, 0), # Move up
        (-1, 0) # Move down
    ]
    adjList = []
    posMatrix = []
    nodeList = []
    with open(file, "r") as f: # Read the file into lines
        lines = f.readlines()
        newlines = [] # The new lines
        for line in lines:
            newlines.append(line.replace('\n', '')) # Delete the new lines symbol

        # Some uninteresting stuff
        height = len(newlines)
        #width = len(newlines[0])

        # Fill up the matrix
        for i in range(height):
            posMatrix.append([])

        # Creation of the actual list of faking adjacency list - reading each node without neighbours
        for yindex, line in enumerate(newlines): # For each line in the maze
            for xindex, char in enumerate(line): # For each position in each line
                nodeInfo = None
                isGoal = False # Keep register of if it's the goal node
                isStart = False

                if (char == 'B'):
                    isGoal = True
                
                if (char == 'A'):
                    isStart = True
                
                if (char == ' ' or char == 'A' or char == 'B'):
                    nodeInfo = GraphNode(len(nodeList) + 1, isGoal, isStart)
                
                # TODO: Stuff the adjacency shit

                # Add the created note into the matrix
                posMatrix[yindex].append((nodeInfo.getNumber() if nodeInfo is not None else None))

                if (nodeInfo is not None):
                    nodeList.append((nodeInfo, (yindex, xindex)))

    # Reading the neighbours for each read node
    for nodeInfo in nodeList:
        neighbours = []
        currentPos = nodeInfo[1]

        # Check if there are any nodes on the neighbourhood
        for i in range(0, len(avMoves)):
            try:
                rValue = posMatrix[currentPos[0] + avMoves[i][0]][currentPos[1] + avMoves[i][1]]
                if (rValue is not None):
                    for el in nodeList:
                        if el[0].getNumber() == rValue:
                            neighbours.append(el[0])
            except Exception:
                continue
        
        # Add the found neighbours into the node
        node = nodeInfo[0]

        for neigh in neighbours:
            node.pushNeighbour(neigh)

        # Add the node to the adjacency list
        adjList.append(node)
        """
        # Add the found neighbours into the adjacency list
        newAdjacency = [nodeInfo[0]]
        neighTuple = []
        for el in neighbours:
            neighTuple.append(el) # Add the found neighbour to the adjacent list

        newAdjacency.append(neighTuple) 
        adjList.append(newAdjacency)
        """

    if printMatrix:
        printAdjacency(posMatrix)

    return adjList