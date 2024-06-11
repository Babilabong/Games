import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 750

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Tic-Tac-Toe Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)

TITLE_FONT = pygame.font.SysFont("comicsans", 30)
SMALL_FONT = pygame.font.SysFont("arial", 30)
BIG_FONT = pygame.font.SysFont("arial", 180)

player = ["X", "O"]
player_paint = [RED, BLUE]


def creat_board():
    dim = 3
    board = [[[[" " for _ in range(dim)] for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
    return board


def fill_size_board():
    inner_row = []
    inner_board = []
    row = []
    board = []
    base_x = 130
    base_y = 130
    for r in range(3):
        for c in range(3):

            for i in range(3):
                for j in range(3):
                    inner_row.append((base_x + (195 * c) + (55 * j), base_y + (195 * r) + (55 * i)))
                inner_board.append(inner_row)
                inner_row = []
            row.append(inner_board)
            inner_board = []
        board.append(row)
        row = []

    return board


def draw_base_board(x, y, w, h, letter_size, space, color):
    pygame.draw.rect(WIN, color, (x + space + letter_size, y + space, w, h))
    pygame.draw.rect(WIN, color, (x + 2*(space + letter_size), y + space, w, h))
    pygame.draw.rect(WIN, color, (x + space, y + space + letter_size, h, w))
    pygame.draw.rect(WIN, color, (x + space, y + 2*(space + letter_size), h, w))


def draw_board(turn, game_board, text, lock_board):
    if lock_board == (-1, -1):
        draw_text = TITLE_FONT.render(text, 1, player_paint[turn % 2])
        WIN.blit(draw_text, ((WIDTH-draw_text.get_width())//2, 30))
    else:
        draw_text = TITLE_FONT.render(text + " row = " + str(lock_board[0]+1) + " col = " + str(lock_board[1]+1), 1, player_paint[turn % 2])
        WIN.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, 30))

    draw_base_board(100, 100, 15, 570, 180, 15, WHITE)

    for i in range(3):
        for j in range(3):
            if game_board[i][j] == "X":
                draw_text = BIG_FONT.render("X", 1, RED)
                WIN.blit(draw_text, (140 + j*195, 105 + i*195))
            elif game_board[i][j] == "O":
                draw_text = BIG_FONT.render("O", 1, BLUE)
                WIN.blit(draw_text, (135 + j * 195, 105 + i * 195))
            elif game_board[i][j] == "T":
                draw_text = BIG_FONT.render("T", 1, WHITE)
                WIN.blit(draw_text, (140 + j * 195, 105 + i * 195))
            else:
                if lock_board[0] == i and lock_board[1] == j:
                    color = GREEN
                else:
                    color = WHITE
                draw_base_board(115 + j*195, 115 + i*195, 15, 150, 40, 15, color)

                for r in range(3):
                    for c in range(3):
                        if game_board[i][j][r][c] == "X":
                            draw_text = SMALL_FONT.render("X", 1, RED)
                            WIN.blit(draw_text, (140 + j * 195 + c * 55, 133 + i * 195 + r * 55))
                        elif game_board[i][j][r][c] == "O":
                            draw_text = SMALL_FONT.render("O", 1, BLUE)
                            WIN.blit(draw_text, (138 + j * 195 + c * 55, 133 + i * 195 + r * 55))


def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ('X', 'O'):
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ('X', 'O'):
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ('X', 'O'):
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ('X', 'O'):
        return board[0][2]

    # No winner found
    return ' '


def tie_check(board):
    if board in ('X', 'O'):
        return False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ('X', 'O', 'T'):
                return False
    return True


def game():
    game_board = creat_board()
    game_size_board = fill_size_board()
    runing = True
    turn = 0
    lock_board = (-1, -1)
    clock = pygame.time.Clock()
    while runing:
        clock.tick(FPS)
        WIN.fill(BLACK)
        text = str(player[turn % 2]) + " player turn - choose spot"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for r in range(3):
                    for c in range(3):
                        if game_board[r][c] != 'X' and game_board[r][c] != 'O' and game_board[r][c] != 'T':
                            for i in range(3):
                                for j in range(3):
                                    if (game_size_board[r][c][i][j][0] <= x <= (game_size_board[r][c][i][j][0]+40)) and (game_size_board[r][c][i][j][1] <= y <= (game_size_board[r][c][i][j][1]+40)):
                                        if lock_board == (-1, -1) or (r == lock_board[0] and c == lock_board[1]):
                                            if game_board[r][c][i][j] == " ":
                                                game_board[r][c][i][j] = player[turn % 2]
                                                lock_board = (i, j)
                                                if game_board[lock_board[0]][lock_board[1]] in ('X', 'O', 'T'):
                                                    lock_board = (-1, -1)
                                                turn += 1

                            winner = check_winner(game_board[r][c])
                            if winner != " ":
                                game_board[r][c] = winner
                                if lock_board[0] == r and lock_board[1] == c:
                                    lock_board = (-1, -1)

                            if tie_check(game_board[r][c]):
                                game_board[r][c] = 'T'
                                if lock_board[0] == r and lock_board[1] == c:
                                    lock_board = (-1, -1)

        winner = check_winner(game_board)
        if winner != " ":
            lock_board = (-1, -1)
            text = winner + " WON THE GAME!"
            turn += 1

        draw_board(turn, game_board, text, lock_board)
        pygame.display.update()

        if winner != " ":
            pygame.time.delay(1500)
            WIN.fill(BLACK)
            draw_text = TITLE_FONT.render(winner + " WON THE GAME!", 1, WHITE)
            WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1500)
            pygame.quit()
            return 0

        if board_full(game_board):
             if tie_check(game_board):
                WIN.fill(BLACK)
                draw_text = TITLE_FONT.render("TIE GAME!", 1, WHITE)
                WIN.blit(draw_text,
                        (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                return 0


if __name__ == "__main__":
    game()