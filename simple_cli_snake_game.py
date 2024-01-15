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
