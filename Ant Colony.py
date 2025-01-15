import numpy as np
import random

grid_size = 6
grid = np.zeros((grid_size, grid_size), dtype=str)
grid[:] = '.'  #empty spaces
grid[0, 0] = 'H'  #hive
grid[5, 5] = 'F'  #food


#randomly place obstacles
num_obstacles = 8
obstacles = set()
while len(obstacles) < num_obstacles:
    x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    if (x, y) not in [(0, 0), (5, 5)] and grid[x, y] != 'X':
        grid[x, y] = 'X'
        obstacles.add((x, y))


#separate grid for phermones
pheromone_grid = np.zeros((grid_size, grid_size))  # Start with no pheromones
max_pheromone_level = 50  # Cap for maximum pheromone level


#ants & phermones initialization
num_ants = 4
pheromone_strength = 10  #pheromone units added when finding food
pheromone_decay_rate = 0.05  #decay rate (to be ajusted)


class Ant:
    def __init__(self):
        self.position = (0, 0)  #start at hive
        self.path = []  #track path to leave pheromones on return
        self.found_food = False  # tack if ant has found food


    def move(self):
        x, y = self.position
        neighbors = self.get_neighbors(x, y)


        #follow pheromones or choose randomly if undecided
        if neighbors:
            pheromones = [pheromone_grid[nx, ny] for nx, ny in neighbors]
            max_pheromone = max(pheromones)
            if max_pheromone == 0:  #no pheromones to follow
                next_pos = random.choice(neighbors)
            else:
                next_pos = neighbors[pheromones.index(max_pheromone)]
        else:
            next_pos = self.position


        #move to selected position
        self.position = next_pos
        if not self.found_food:
            self.path.append(self.position)  #record path only before finding food


        #handle collisions with obstacles
        if grid[self.position] == 'X':
            self.position = random.choice(neighbors)


    def get_neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #up | Down | Left | Right
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx, ny] != 'X':
                neighbors.append((nx, ny))
        return neighbors


#simulation Setup
ants = [Ant() for _ in range(num_ants)]
time_steps = 30


#loop simulation
for t in range(time_steps):
    for ant in ants:
        if ant.position == (5, 5):  #if the ant reaches the food
            if not ant.found_food:  #only leave pheromones on the first discovery
                #increase pheromones along the path back to the hive
                for pos in ant.path:
                    pheromone_grid[pos] += pheromone_strength
                    pheromone_grid[pos] = min(pheromone_grid[pos], max_pheromone_level)  # Cap pheromone level
                ant.found_food = True  #mark as found food
            ant.path = []  #reset path
            ant.position = (0, 0)  #return to hive
        else:
            ant.move()


    #apply pheromone decay
    pheromone_grid = np.maximum(pheromone_grid * (1 - pheromone_decay_rate), 0)


    #priting grid & ants
    print(f"Time Step {t+1}: Grid State")
    for i in range(grid_size):
        row = ''
        for j in range(grid_size):
            if (i, j) in [ant.position for ant in ants]:
                row += 'A '
            elif grid[i, j] == 'X':
                row += 'X '
            elif grid[i, j] == 'H':
                row += 'H '
            elif grid[i, j] == 'F':
                row += 'F '
            else:
                row += '. '
        print(row)

    print(f"Pheromone Grid at Time Step {t+1}:")
    for i in range(grid_size):
        row = ""
        for j in range(grid_size):
            row += f"{pheromone_grid[i, j]:.1f} "
        print(row)
    print("\n")