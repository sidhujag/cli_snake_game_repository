import random
import curses

BOARD_WIDTH = 20
BOARD_HEIGHT = 15
GAME_SPEED = 100  # The lower the number, the faster the game speed.

def init_snake(width, height):
    return [(width // 4, height // 2)]

def create_board(width, height):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    return board

def place_food(board, width, height, snake):
    empty = False
    while not empty:
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        if (x, y) not in snake and board[y][x] == ' ':
            board[y][x] = '*'
            empty = True
    return (x, y)

def print_board(stdscr, board, score):
    stdscr.clear()
    for row in board:
        stdscr.addstr(''.join(row) + '\n')
    stdscr.addstr(f'Score: {score}\n')
    stdscr.refresh()

def get_next_position(head, direction):
    x, y = head
    if direction == curses.KEY_RIGHT:
        x += 1
    elif direction == curses.KEY_LEFT:
        x -= 1
    elif direction == curses.KEY_UP:
        y -= 1
    elif direction == curses.KEY_DOWN:
        y += 1
    return x, y

def is_opposite_direction(current, new):
    opposite_pairs = {
        (curses.KEY_UP, curses.KEY_DOWN),
        (curses.KEY_DOWN, curses.KEY_UP),
        (curses.KEY_LEFT, curses.KEY_RIGHT),
        (curses.KEY_RIGHT, curses.KEY_LEFT),
    }
    return (current, new) in opposite_pairs or (new, current) in opposite_pairs

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(GAME_SPEED)

    width, height = BOARD_WIDTH, BOARD_HEIGHT
    board = create_board(width, height)
    snake = init_snake(width, height)
    direction = curses.KEY_RIGHT
    score = 0

    # Place the first food on the board
    food = place_food(board, width, height, snake)

    while True:
        key = stdscr.getch()

        # Update the direction based on user input
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            if not is_opposite_direction(direction, key):
                direction = key

        head = snake[0]
        new_head = get_next_position(head, direction)

        # Check for collision with walls or self to end the game
        if (new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height or
            new_head in snake):
            stdscr.addstr(height // 2, width // 2 - len("Game Over") // 2, "Game Over")
            stdscr.nodelay(0)
            stdscr.getch()
            break

        snake.insert(0, new_head)

        # Check if new head position has food
        if new_head == food:
            food = place_food(board, width, height, snake)
            score += 1
        else:
            tail = snake.pop()
            board[tail[1]][tail[0]] = ' '

        board[new_head[1]][new_head[0]] = '#'
        print_board(stdscr, board, score)

if __name__ == '__main__':
    curses.wrapper(main)
def create_snake(screen_width, screen_height):
    # Initial snake co-ordinates
    snake = [[screen_height//2, screen_width//4]]
    return snake

def create_food(screen_width, screen_height, snake):
    food = None
    while food is None:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food in snake:  # Prevent food from spawning on the snake
            food = None
    return food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = create_snake(screen_width, screen_height)
    food = create_food(screen_width, screen_height, snake)

    score = 0
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over")
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

        # Check if snake has eaten the food
        if snake[0] == food:
            score += 1
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        print_score(stdscr, score)
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], '#')
            food = create_food(screen_width, screen_height, snake)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '*')
        print_score(stdscr, score)

        stdscr.addch(food[0], food[1], '*')
        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(stdscr, len(snake) - 1)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def create_snake(screen_width, screen_height):
    # Initial snake co-ordinates
    snake = [[screen_height//2, screen_width//4]]
    return snake

def create_food(screen_width, screen_height, snake):
    food = None
    while food is None:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food in snake:  # Prevent food from spawning on the snake
            food = None
    return food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = create_snake(screen_width, screen_height)
    food = create_food(screen_width, screen_height, snake)

    score = 0
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over")
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

        # Check if snake has eaten the food
        if snake[0] == food:
            score += 1
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(stdscr, score)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def create_snake(screen_width, screen_height):
    # Initial snake co-ordinates
    snake = [[screen_height//2, screen_width//4]]
    return snake

def create_food(screen_width, screen_height, snake):
    food = None
    while food is None:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food in snake:  # Prevent food from spawning on the snake
            food = None
    return food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = create_snake(screen_width, screen_height)
    food = create_food(screen_width, screen_height, snake)

    score = 0
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over")
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

        # Check if snake has eaten the food
        if snake[0] == food:
            score += 1
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(stdscr, score)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def create_snake(screen_width, screen_height):
    # Initial snake co-ordinates
    snake = [[screen_height//2, screen_width//4]]
    return snake

def create_food(screen_width, screen_height, snake):
    food = None
    while food is None:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food in snake:  # Prevent food from spawning on the snake
            food = None
    return food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = create_snake(screen_width, screen_height)
    food = create_food(screen_width, screen_height, snake)

    score = 0
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over")
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

        # Check if snake has eaten the food
        if snake[0] == food:
            score += 1
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(stdscr, score)

if __name__ == "__main__":
    curses.wrapper(game)
