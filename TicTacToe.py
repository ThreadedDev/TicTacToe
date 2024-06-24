import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

# Define fonts
GAME_FONT = pygame.font.SysFont('Comic Sans MS', 100)

# Initialize game variables
player = 1
game_over = False
winner = None
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + 15, row * SQUARE_SIZE + 15), 
                                 ((col + 1) * SQUARE_SIZE - 15, (row + 1) * SQUARE_SIZE - 15), 15)
                pygame.draw.line(screen, BLACK, ((col + 1) * SQUARE_SIZE - 15, row * SQUARE_SIZE + 15), 
                                 (col * SQUARE_SIZE + 15, (row + 1) * SQUARE_SIZE - 15), 15)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                                   row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 15, 15)

def check_win():
    global winner, game_over
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            winner = board[row][0]
            game_over = True
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            winner = board[0][col]
            game_over = True
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        winner = board[0][0]
        game_over = True
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        winner = board[0][2]
        game_over = True
        return True
    # Check draw
    if all(all(cell != '' for cell in row) for row in board):
        game_over = True
        return True
    return False

def draw_winner(winner):
    if winner:
        win_text = GAME_FONT.render(f"Player {winner} wins!", True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
    else:
        draw_text = GAME_FONT.render("It's a draw!", True, BLACK)
        screen.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))

def mark_square(row, col):
    global player
    if board[row][col] == '' and not game_over:
        if player == 1:
            board[row][col] = 'X'
            player = 2
        elif player == 2:
            board[row][col] = 'O'
            player = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            mark_square(clicked_row, clicked_col)
            check_win()

    screen.fill(WHITE)
    draw_lines()
    draw_figures()

    if game_over:
        draw_winner(winner)

    pygame.display.update()
