# Conway's Game of LIfe
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append('') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True: # Main program loop
    print('\n\n\n\n\n') # Seperate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Pring currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space
        print() # Print newline at end of row

    # Calculate next step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `%WIDTH` ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #Count # of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] =='#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right alive

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells w/ 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '' and numNeighbors == 3:
                # Dead cells w/ 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ''
    time.sleep(1) # Add a 1 sec pause reduce flickering.