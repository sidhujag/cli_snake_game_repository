import unittest
from unittest.mock import patch
from cli_snake_game import create_snake, create_food, print_score, game
import curses

class TestCLISnakeGame(unittest.TestCase):

    def test_create_snake(self):
        screen_width, screen_height = 20, 10
        snake = create_snake(screen_width, screen_height)
        self.assertEqual(snake, [[screen_height//2, screen_width//4]])

    def test_create_food(self):
        screen_width, screen_height = 20, 10
        snake = [[5, 5]]
        with patch('random.randint', side_effect=[5, 5, 6, 6]):
            food = create_food(screen_width, screen_height, snake)
            self.assertNotEqual(food, [5, 5])
            self.assertEqual(food, [6, 6])

    @patch('curses.stdscr')
    def test_print_score(self, mock_stdscr):
        print_score(mock_stdscr, 5)
        mock_stdscr.addstr.assert_called_with(0, 2, 'Score: 5')

    @patch('curses.stdscr')
    def test_game_over_conditions(self, mock_stdscr):
        screen_height, screen_width = 20, 10
        mock_stdscr.getmaxyx.return_value = (screen_height, screen_width)
        mock_stdscr.getch.return_value = -1
        snake = [[0, 0]]
        with patch('cli_snake_game.create_snake', return_value=snake):
            with patch('cli_snake_game.create_food', return_value=[5, 5]):
                with self.assertRaises(SystemExit):
                    game(mock_stdscr)
                mock_stdscr.addstr.assert_called_with(screen_height//2, screen_width//2 - len("Game Over")//2, "Game Over")

    # Additional tests for movement, food consumption, and score updates can be added here.

if __name__ == '__main__':
    unittest.main()
