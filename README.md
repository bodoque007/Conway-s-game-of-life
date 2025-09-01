# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame.

## Requirements

- Python 3.10 or higher
- Pygame

## Installation

1. Clone the repository
2. Install the required dependencies with the following command:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the following on your terminal:

```bash
python conway.py
```

## How to Play

1. **Select initial cells**: Click on cells to create the initial living cells
2. **Start simulation**: Press SPACE to begin the simulation
3. **Toggle instructions**: Press TAB to show/hide the instruction panel
4. **Quit**: Press 'q' to quit at any time
5. **Restart**: When the game ends, press SPACE to restart or 'q' to quit

## Game Rules

Conway's Game of Life follows these simple rules:

- Any live cell with 2 or 3 live neighbors survives
- Any dead cell with exactly 3 live neighbors becomes a live cell
- All other live cells die in the next generation
- All other dead cells stay dead
