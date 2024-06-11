import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 750

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 step Tic-Tac-Toe Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
D_RED = (100, 0, 0)
D_BLUE = (0, 0, 100)

TITLE_FONT = pygame.font.SysFont("comicsans", 30)
SMALL_FONT = pygame.font.SysFont("arial", 30)
BIG_FONT = pygame.font.SysFont("arial", 180)

player = ["X", "O"]
player_paint = [RED, BLUE]


def draw_board(game_board, turn, text):
    pygame.draw.rect(WIN, WHITE, (295, 115, 15, 570))
    pygame.draw.rect(WIN, WHITE, (195+295, 115, 15, 570))
    pygame.draw.rect(WIN, WHITE, (115, 295, 570, 15))
    pygame.draw.rect(WIN, WHITE, (115, 295+195, 570, 15))

    draw_text = TITLE_FONT.render(text, 1, player_paint[turn % 2])
    WIN.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, 30))

    if turn > 5:
        delete = turn - 6
    else:
        delete = -1

    for row in range(3):
        for col in range(3):
            if game_board[row][col] != " ":
                if game_board[row][col][1] == delete:
                    if game_board[row][col][0] == 'X':
                        draw_text = BIG_FONT.render("X", 1, D_RED)
                        WIN.blit(draw_text, (140 + col * 195, 105 + row * 195))
                    elif game_board[row][col][0] == 'O':
                        draw_text = BIG_FONT.render("O", 1, D_BLUE)
                        WIN.blit(draw_text, (135 + col * 195, 105 + row * 195))
                else:
                    if game_board[row][col][0] == 'X':
                        draw_text = BIG_FONT.render("X", 1, RED)
                        WIN.blit(draw_text, (140 + col * 195, 105 + row * 195))
                    elif game_board[row][col][0] == 'O':
                        draw_text = BIG_FONT.render("O", 1, BLUE)
                        WIN.blit(draw_text, (135 + col * 195, 105 + row * 195))


def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row[0] != " " and row[1] != " " and row[2] != " ":
            if row[0][0] == row[1][0] == row[2][0]:
                return row[0][0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] != " " and board[1][col] != " " and board[2][col] != " ":
            if board[0][col][0] == board[1][col][0] == board[2][col][0]:
                return board[0][col][0]

    # Check diagonals for a winner
    if board[0][0] != " " and board[1][1] != " " and board[2][2] != " ":
        if board[0][0][0] == board[1][1][0] == board[2][2][0]:
            return board[0][0][0]
    if board[2][0] != " " and board[1][1] != " " and board[0][2] != " ":
        if board[2][0][0] == board[1][1][0] == board[0][2][0]:
            return board[2][0][0]

    # No winner found
    return ' '



def game():
    game_board = []
    row = []
    for i in range(3):
        for j in range(3):
            row.append(" ")
        game_board.append(row)
        row = []

    clock = pygame.time.Clock()
    turn = 0
    while(True):
        clock.tick(FPS)
        WIN.fill(BLACK)
        text = str(player[turn % 2]) + " player turn - choose spot"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(3):
                    for j in range(3):
                        if 115 + (j*195) <= x <= 115 + (j*195) + 180 and 115 + (i*195) <= y <= 115 + (i*195) + 180 and game_board[i][j] == " ":
                            game_board[i][j] = (str(player[turn % 2]),turn)
                            turn += 1

                for i in range(3):
                    for j in range(3):
                        if game_board[i][j] != " ":
                            if game_board[i][j][1] < turn - 6:
                                game_board[i][j] = " "

        winner = check_winner(game_board)
        if winner != " ":
            text = winner + " won!"
            turn -= 1

        draw_board(game_board,turn,text)
        pygame.display.update()

        if winner != " ":
            pygame.time.delay(2500)
            pygame.quit()
            return 0






if __name__ == "__main__":
    game()
