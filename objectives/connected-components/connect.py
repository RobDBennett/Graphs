islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands):
    visited = set()
    counter = 0
    def get_neighbors(coords):
        neighbors = []
        row, col = coords
        if row > 0 and islands[row-1][col] == 1:
            neighbors.append((row-1, col))
        if row < len(islands) -1 and islands[row+1][col] == 1:
            neighbors.append((row+1, col))
        if col > 0 and islands[row][col-1] == 1:
            neighbors.append((row, col-1))
        if col < len(islands[row]) -1 and islands[row][col+1] == 1:
            neighbors.append((row, col+1))
        

        return neighbors

    def bft(row, col):
        q = []
        q.append((row, col))
        while len(q) > 0:
            coords = q.pop(0)
            if coords not in visited:
                visited.add(coords)
                for neighbor in get_neighbors((row, col)):
                    q.append(neighbor)

    for row in range(len(islands)):
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            coords = (row, col)
            if coords not in visited and node_val == 1:
                bft(row,col)
                counter += 1
    return counter