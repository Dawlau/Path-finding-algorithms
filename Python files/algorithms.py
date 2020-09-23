from constants import moveRow, moveCol, delay

def buildPath(From, grid, start, stop):

    import colors

    Stack = []
    cell = From[stop[0]][stop[1]]
    prev = stop

    while cell != start:

        direction = None
        for dir in range(len(moveRow)):
            if (cell[0] + moveRow[dir], cell[1] + moveCol[dir]) == prev:
                if dir == 0:
                    direction = "up"
                elif dir == 1:
                    direction = "right"
                elif dir == 2:
                    direction = "down"
                else:
                    direction = "left"

        Stack.append((cell, direction))

        prev = cell
        cell = From[cell[0]][cell[1]]

    while len(Stack):
        cell, direction = Stack[-1]
        row, col = cell
        Stack.pop()
        grid[row][col].changeColor(colors.white)
        grid[row][col].addArrow(direction)



def Dijkstra():
    print("Dijkstra")



def Bfs(grid, start, stop, showSteps):

    from collections import deque
    import colors, utilities, time, pygame

    rows = len(grid)
    cols = len(grid[0])

    Deque = deque()

    seen = [] * rows
    From = [] * rows

    for row in range(rows):
        seen.append([False] * cols)
        From.append([None] * cols)

    Deque.append(start)
    seen[start[0]][start[1]] = True

    while len(Deque):

        row, col = Deque.popleft()

        if showSteps and (row, col) != start and (row, col) != stop:
            grid[row][col].changeColor(colors.green)
            pygame.display.flip()
            time.sleep(delay)

        for dir in range(len(moveRow)):
            newRow = row + moveRow[dir]
            newCol = col + moveCol[dir]

            if utilities.inGrid(grid, newRow, newCol) and not seen[newRow][newCol] and grid[newRow][newCol].color != colors.black:
                seen[newRow][newCol] = True
                From[newRow][newCol] = (row, col)
                Deque.append((newRow, newCol))

                if (newRow, newCol) == stop:
                    Deque.clear()
                    break

    if not seen[stop[0]][stop[1]]:
        return 0

    buildPath(From, grid, start, stop)

    return 1


def Dfs(grid, start, stop, showSteps):

    import utilities, colors, pygame, time

    rows = len(grid)
    cols = len(grid[0])
    
    seen = [] * rows
    From = [] * rows

    for row in range(rows):
        seen.append([False] * cols)
        From.append([None] * cols)

    Stack = []
    Stack.append(start)
    seen[start[0]][start[1]] = True

    while len(Stack):
        row, col = Stack.pop()

        if showSteps and (row, col) != start and (row, col) != stop:
            grid[row][col].changeColor(colors.green)
            pygame.display.flip()
            time.sleep(delay)

        for dir in range(len(moveRow)):
            newRow = row + moveRow[dir]
            newCol = col + moveCol[dir]

            if utilities.inGrid(grid, newRow, newCol) and not seen[newRow][newCol] and grid[newRow][newCol].color != colors.black:
                seen[newRow][newCol] = True
                From[newRow][newCol] = (row, col)
                Stack.append((newRow, newCol))

                if (newRow, newCol) == stop:
                    Stack.clear()
                    break

    buildPath(From, grid, start, stop)


def Astar():
    pass


def GreedyBestfs():
    pass