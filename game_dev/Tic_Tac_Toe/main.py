import pygame, sys
import numpy as np

pygame.init()

WIDTH = 400
HEIGHT = WIDTH

LINE_WIDTH = 15

# board of the numpy func
BOARD_ROWS = 3
BOARD_COLS = 3

SQUARE_SIZE = int(WIDTH // BOARD_ROWS)

# circle ( o )
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15

# cross ( x )
CROSS_WIDTH = 25
 
# space between cross and square 
SPACE = SQUARE_SIZE // 4

# colors
BG_COLOR = (28, 170, 156)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# 4 main lines
LINE_COLOR = (13, 161, 146)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vetical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, WIDTH), LINE_WIDTH)
    # 2 vetical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, WIDTH), LINE_WIDTH)

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vetical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vetical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def mark_square(row_index, col_index, player):
    # mark_square(0, 0, 1) mean the first square will be marked
    board[row_index][col_index] = player

def draw_figures(row_index, col_index):
    if board[row_index][col_index] == 2:
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(col_index * SQUARE_SIZE + SQUARE_SIZE // 2), int(row_index * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
    elif board[row_index][col_index] == 1:
        pygame.draw.line(screen, CROSS_COLOR, (col_index * SQUARE_SIZE + SPACE, row_index * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                        (col_index * SQUARE_SIZE + SQUARE_SIZE - SPACE, row_index * SQUARE_SIZE + SPACE), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (col_index * SQUARE_SIZE + SPACE, row_index * SQUARE_SIZE + SPACE), 
                        (col_index * SQUARE_SIZE + SQUARE_SIZE - SPACE, row_index * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def available_square(row_index, col_index):
    return board[row_index][col_index] == 0

def is_board_full():
    for row_index in range(BOARD_ROWS):
        for col_index in range(BOARD_COLS):
            if board[row_index][col_index] == 0:
                return False
    return True

def check_win(player):
    # check vertical win
    for col_index in range(BOARD_COLS):
        if board[0][col_index] == player and board[1][col_index] == player and board[2][col_index] == player:
            daw_vertical_winning_line(col_index, player)
            return True
    
    # check horizontal win
    for row_index in range(BOARD_COLS):
        if board[row_index][0] == player and board[row_index][1] == player and board[row_index][2] == player:
            draw_horizontal_winning_line(row_index, player)
            return True

    # check asc diagonal win
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        daw_asc_diagonal_winning_line(player)
        return True

    # check desc diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        daw_desc_diagonal_winning_line(player)
        return True

    return False

def player_color(player):
    color = CROSS_COLOR
    if player == 2:
        color = CIRCLE_COLOR
    return color

def daw_vertical_winning_line(col_index, player):
    # move x to mid
    posX = col_index * SQUARE_SIZE + SQUARE_SIZE // 2
    
    pygame.draw.line(screen, player_color(player), (posX, 15), (posX, HEIGHT - 15), 15)
        
def draw_horizontal_winning_line(row_index, player):
    posY = row_index * SQUARE_SIZE + SQUARE_SIZE // 2
    
    pygame.draw.line(screen, player_color(player), (15, posY), (WIDTH - 15, posY), 15)
    
def daw_desc_diagonal_winning_line(player):
    pygame.draw.line(screen, player_color(player), (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def daw_asc_diagonal_winning_line(player):
    pygame.draw.line(screen, player_color(player), (WIDTH - 15, 15), (15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row_index in range(BOARD_ROWS):
        for col_index in range(BOARD_COLS):
            board[row_index][col_index] = 0

# ==========init game========
# set background
screen.fill(BG_COLOR)

# create a matrix with all values is 0
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# draw 4 main lines
draw_lines()

# player 1, player 2
player = 1

game_over = False
# ==========init game========

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX, mouseY = event.pos[0], event.pos[1]
            clicked_row, clicked_col = int(mouseY // SQUARE_SIZE), int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                # mark in board
                mark_square(clicked_row, clicked_col, player)

                # draw
                draw_figures(clicked_row, clicked_col)
                
                if check_win(player):
                    game_over = True
                    # player = 1
                else:
                    player = player % 2 + 1
                
        if event.type == pygame.KEYDOWN and (game_over or is_board_full()):
            game_over = False
            restart()

    pygame.display.update()

