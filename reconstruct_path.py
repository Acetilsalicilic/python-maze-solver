def reconstructPath(initialNode):
    # The path
    path = []

    if initialNode.getParent() is None:
        raise("First element hasn't a parent")
    
    currentNode = initialNode

    while currentNode.getParent() is not None:
        path.append(currentNode.getNumber()) # Add it to the path
        currentNode = currentNode.getParent() # Go to the parent
    
    path.append(currentNode.getNumber())
    path.reverse()
    
    return path