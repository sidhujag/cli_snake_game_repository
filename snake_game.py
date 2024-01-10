import random
import curses

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
    snake = [(width // 2, height // 2)]
    direction = curses.KEY_RIGHT

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
        else:
            tail = snake.pop()
            board[tail[1]][tail[0]] = ' '
            board[new_head[1]][new_head[0]] = '#'

        print_board(stdscr, board)


if __name__ == '__main__':
    curses.wrapper(main)
