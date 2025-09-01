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
show_instructions = True

pygame.init()
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's game of life")
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_screen(instructions=None):
    global show_instructions
    if instructions is None:
        instructions = show_instructions
        
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
    
    if instructions:
        font = pygame.font.Font(None, 24)
        instructions_lines = [
            "1) Select beginning cells",
            "2) Press SPACE to start simulation", 
            "3) Press 'q' to quit",
            "4) Press TAB to toggle instructions"
        ]
        
        # Calculate background size
        max_width = 0
        total_height = 0
        line_height = 25
        for line in instructions_lines:
            text_surface = font.render(line, True, WHITE)
            max_width = max(max_width, text_surface.get_width())
            total_height += line_height
        
        # Add padding
        padding = 10
        bg_width = max_width + 2 * padding
        bg_height = total_height + 2 * padding
        
        # Draw black background
        pygame.draw.rect(screen, BLACK, (5, 5, bg_width, bg_height))
        pygame.draw.rect(screen, WHITE, (5, 5, bg_width, bg_height), 2)
        
        # Draw instructions text
        y_offset = 15
        for line in instructions_lines:
            draw_text(line, font, WHITE, screen, 15, y_offset)
            y_offset += line_height
    
    clock.tick(5)
    pygame.display.flip()

def user_select_initial_cells():
    global show_instructions
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                elif event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_TAB:
                    show_instructions = not show_instructions
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if 0 <= row < N and 0 <= column < M:
                    grid[row][column] = 1
        draw_screen()
    return True

def neighbors(x, y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            
            ni = (i + N) % N
            nj = (j + M) % M

            if grid[ni][nj] == 1:
                count += 1
    return count

def conway():
    global grid, show_instructions
    done = False
    while not done:
        new_grid = [[0 for _ in range(M)] for _ in range(N)]
        alive_cells = 0
        for x in range(N):
            for y in range(M):
                n_count = neighbors(x, y)
                if grid[x][y] == 1:
                    if n_count == 2 or n_count == 3:
                        new_grid[x][y] = 1
                        alive_cells += 1
                elif grid[x][y] == 0 and n_count == 3:
                    new_grid[x][y] = 1
                    alive_cells += 1
        
        if alive_cells == 0:
            return True
        
        if new_grid == grid:
            return True
        
        grid = new_grid
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_TAB:
                    show_instructions = not show_instructions

        draw_screen()
    return True

def main_game_loop():
    global grid, show_instructions
    running = True
    while running:
        grid = [[0 for _ in range(N)] for _ in range(M)]
        show_instructions = True
        
        if not user_select_initial_cells():
            running = False
            continue
            
        game_over = conway()

        if game_over:
            draw_screen()
            font = pygame.font.Font(None, 40)
            draw_text("Game Over! Press SPACE to restart or 'q' to quit.", font, RED, screen, 100, 500)
            pygame.display.flip()

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            waiting_for_input = False
                        elif event.key == pygame.K_q:
                            running = False
                            waiting_for_input = False
                    elif event.type == pygame.QUIT:
                        running = False
                        waiting_for_input = False

if __name__ == "__main__":
    main_game_loop()
    pygame.quit()