# Ant Colony Simulation with Pheromones

This project simulates the behavior of ants navigating a 2D grid in search of food. Ants leave pheromones along their path to guide others, demonstrating emergent colony behavior. The grid includes obstacles, a hive, and a food source, creating a dynamic environment for exploration.

---

## Features

### Environment
- **Grid**:
  - A `6x6` grid with predefined locations for:
    - Hive (`H`) at `(0, 0)`.
    - Food (`F`) at `(5, 5)`.
    - Obstacles (`X`) randomly placed across the grid.
  - Empty spaces represented by `.`.
- **Pheromone Grid**:
  - A separate grid tracks pheromone levels.
  - Pheromones decay over time but accumulate along paths to food.

### Ant Behavior
- **Movement**:
  - Ants start at the hive and move to neighboring cells.
  - Decisions prioritize cells with higher pheromone levels but allow randomness.
- **Food Discovery**:
  - When an ant reaches the food, it leaves a pheromone trail along its path back to the hive.
- **Collisions**:
  - Ants avoid obstacles and choose alternative paths when blocked.

### Pheromone Dynamics
- **Pheromone Strength**:
  - Pheromones are deposited with a fixed strength (`10`) when food is found.
  - Maximum pheromone level is capped at `50`.
- **Decay**:
  - Pheromone levels decay by `5%` at each time step.

### Simulation Output
- Tracks ant positions, grid state, and pheromone grid for each time step.
- Prints the state of the grid and pheromone grid after every time step.

---

## Simulation Workflow

1. **Initialization**:
   - The grid is populated with a hive, food, and obstacles.
   - Ants are created and start at the hive.
2. **Time Steps**:
   - Ants move towards the food, guided by pheromones and randomness.
   - Upon finding food, ants leave a pheromone trail and return to the hive.
   - Pheromones decay across the grid.
3. **Output**:
   - The state of the grid and pheromone levels are displayed after each time step.

---

## Code Structure

### Key Classes and Functions

#### **Ant Class**
- **Attributes**:
  - `position`: Current position of the ant.
  - `path`: Tracks the ant's movement path.
  - `found_food`: Indicates whether the ant has found food.
- **Methods**:
  - `move`: Moves the ant to a neighboring cell based on pheromone levels and obstacles.
  - `get_neighbors`: Returns valid neighboring cells for movement.

#### **Simulation Logic**
- **Initialization**:
  - Sets up the grid, pheromone grid, and obstacles.
  - Creates ants starting at the hive.
- **Movement**:
  - Ants move based on pheromone levels and proximity to food.
- **Pheromone Updates**:
  - Pheromones are deposited along paths to food and decay over time.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.
- Required libraries:
  ```bash
  pip install numpy
