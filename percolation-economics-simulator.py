# Python code to implement Conway's Game Of Life
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
 
# setting up the values for the grid
STRONG = 2
MODERATE = 1
WEAK = 0
vals = [STRONG, MODERATE, WEAK]
 
def randomGrid(N):
 
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.3, 0.69, 0.01]).reshape(N, N)
 
def update(frameNum, img, grid, N):
 
    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
 
            # compute 8-neighbour sum
            # using periodic boundary conditions
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) + np.random.choice([-12,-6,-2,0,1,7],1,p=[0.07,0.03,0.20,0.50,0.10,0.10]))
 
            # apply rules
            if total > 10:
                newGrid[i, j] = STRONG
            elif total > 5:
                newGrid[i, j] = MODERATE
            else:
                newGrid[i,j] = WEAK
 
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img
 
# main() function
def main():
     
    # set grid size
    N = 600
         
    # set animation update interval
    updateInterval = 200
    
    grid = randomGrid(N)
 
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='RdYlGn')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)
    plt.show()
 
# call main
if __name__ == '__main__':
    main()