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
    pring('\n\n\n\n\n') # Seperate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Pring currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pring(currentCells[x][y], end=') # Print the # or space
        print() # Print newline at end of row
