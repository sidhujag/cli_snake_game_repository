import random
import curses

BOARD_WIDTH = 20
BOARD_HEIGHT = 15
GAME_SPEED = 100  # The lower the number, the faster the game speed.

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(GAME_SPEED)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = [[screen_height//2, screen_width//4]]
    direction = curses.KEY_RIGHT
    score = 0
    food = None
    while food is None:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food in snake:
            food = None

    def print_score(score):
        stdscr.addstr(0, 2, 'Score: ' + str(score))

    while True:
        key = stdscr.getch()

        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Check for collision with walls or self to end the game
        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height // 2, screen_width // 2 - len("Game Over") // 2, "Game Over", curses.A_BOLD)
            stdscr.addstr(height // 2, width // 2 - len("Game Over") // 2, "Game Over")
            stdscr.nodelay(0)
            stdscr.getch()
            break

        new_head = [snake[0][0], snake[0][1]]

        # Check if new head position has food
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
                food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
                if food in snake:
                    food = None
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')
            board[tail[1]][tail[0]] = ' '

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)
def main(stdscr):
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
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)
            food = create_food(screen_width, screen_height, snake)
            stdscr.addch(food[0], food[1], '#')
            food = create_food(screen_width, screen_height, snake)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '*')
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)

        stdscr.addch(food[0], food[1], '*')
        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(stdscr, len(snake) - 1)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def main(stdscr):
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
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over", curses.A_BOLD)
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
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def main(stdscr):
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
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over", curses.A_BOLD)
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
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(game)
import random
import curses

def main(stdscr):
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
            stdscr.addstr(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over", curses.A_BOLD)
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
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], '#')
        print_score(score)

if __name__ == "__main__":
    curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(game)
