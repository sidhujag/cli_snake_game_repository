import random
import curses

def init_snake(width, height):
    return [(width // 4, height // 2)]

def create_board(width, height):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    return board

def place_food(board, width, height):
    empty = False
    while not empty:
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        if board[y][x] == ' ':
            board[y][x] = '*'
            empty = True

def print_board(stdscr, board):
    stdscr.clear()
    for row in board:
        stdscr.addstr(''.join(row) + '\n')
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    width, height = 20, 15
    board = create_board(width, height)
    snake = init_snake(width, height)
    direction = curses.KEY_RIGHT
    score = 0
    score = 0

    place_food(board, width, height)

    while True:
        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = (head[0] + 1, head[1])
        elif direction == curses.KEY_LEFT:
            new_head = (head[0] - 1, head[1])
        elif direction == curses.KEY_UP:
            new_head = (head[0], head[1] - 1)
        elif direction == curses.KEY_DOWN:
            new_head = (head[0], head[1] + 1)

        # Check for collision with walls or self
        if (new_head[0] >= width or new_head[0] < 0 or
            new_head[1] >= height or new_head[1] < 0 or
            new_head in snake):
            break  # Game over

        snake.insert(0, new_head)

        # Check if new head position has food
        if board[new_head[1]][new_head[0]] == '*':
            place_food(board, width, height)
            board[new_head[1]][new_head[0]] = '#'
            score += 1
            score += 1
        else:
            tail = snake.pop()
            board[tail[1]][tail[0]] = ' '
            board[new_head[1]][new_head[0]] = '#'

        print_board(stdscr, board, score)

        print_board(stdscr, board, score)

def print_board(stdscr, board, score):
    stdscr.clear()
    for row in board:
        stdscr.addstr(''.join(row) + '\n')
    stdscr.addstr(f'Score: {score}\n')
    stdscr.refresh()

def print_board(stdscr, board, score):
    stdscr.clear()
    for row in board:
        stdscr.addstr(''.join(row) + '\n')
    stdscr.addstr(f'Score: {score}\n')
    stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
import random
import curses

def create_snake_and_food(screen_width, screen_height):
    snake = [[screen_height//2, screen_width//4]]
    food = [screen_height//2, screen_width//2]
    return snake, food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake, food = create_snake_and_food(screen_width, screen_height)

    score = 0
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2, "Game Over")
            stdscr.nodelay(0)
            stdscr.getch()
            break

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, screen_height-1),
                    random.randint(1, screen_width-1)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], '#')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '*')
        print_score(stdscr, score)

if __name__ == "__main__":
    curses.wrapper(game)
