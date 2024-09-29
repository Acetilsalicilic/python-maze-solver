def printAdjacency(posMatrix):
    # Line register
    lines = []

    for originLine in posMatrix:
        line = ''

        for pos in originLine:
            if pos is None:
                line = line + "#####"
                continue
            if pos < 10:
                line = line + f' {pos}   '
                continue
            if pos >= 10 and pos < 100:
                line = line + f' {pos}  '
                continue
            if pos >= 100:
                line = line + f' {pos} '
                continue
    
        lines.append(line)
    
    for line in lines:
        print(line)