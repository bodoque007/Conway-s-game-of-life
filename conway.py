import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
N = 60
M = 60
WIDTH = 20
HEIGHT = 20
MARGIN = 5


grid = [[0 for _ in range(N)] for _ in range(M)]

pygame.init()
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's game of life")
clock = pygame.time.Clock()

def draw_screen():
    screen.fill(BLACK)
    for row in range(N):
        for column in range(M):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, 
                            color, 
                            [(MARGIN + WIDTH) * column + MARGIN, 
                            (MARGIN + HEIGHT) * row + MARGIN, 
                            WIDTH, 
                            HEIGHT])
    clock.tick(5)
    pygame.display.flip()

def user_select_initial_cells():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                grid[row][column] = 1
        draw_screen()


def neighbors(x, y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if i < 0:
                i = N - 1
            elif i >= N:
                i = 0
            if j < 0:
                j = M - 1
            elif j >= M:
                j = 0
            if grid[i][j] == 1:
                count += 1
    return count

def conway():
    done = False
    while not done:            
        for x in range(N):
            for y in range(M):
                if grid[x][y] == 1:
                    if neighbors(x, y) < 2 or neighbors(x, y) > 3:
                        # Cell dies
                        grid[x][y] = 0
                elif grid[x][y] == 0 and neighbors(x, y) == 3:
                    # Cell revives
                    grid[x][y] = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        draw_screen()


if __name__ == "__main__":
    user_select_initial_cells()
    conway()
    pygame.quit()