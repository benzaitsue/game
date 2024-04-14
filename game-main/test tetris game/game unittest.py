import unittest
from unittest.mock import patch, Mock

from game import Game  


class TestGame(unittest.TestCase):

    def setUp(self):
        pygame_mock = Mock()
        pygame_mock.mixer.Sound.return_value = Mock()
        pygame_mock.mixer.music = Mock()
        pygame_mock.mixer.music.play.return_value = None
        pygame_mock.mixer.music.load.return_value = None
        pygame_mock.mixer.music.play.side_effect = Exception("pygame.mixer.music.play() called unexpectedly")
        pygame_mock.mixer.music.load.side_effect = Exception("pygame.mixer.music.load() called unexpectedly")
        self.pygame_patcher = patch.dict('sys.modules', {'pygame': pygame_mock})
        self.pygame_patcher.start()

    def tearDown(self):
        self.pygame_patcher.stop()

    def test_move_left(self):
        game = Game()
        game.current_block = Mock()
        game.block_inside = Mock(return_value=True)
        game.block_fits = Mock(return_value=True)

        game.move_left()

        game.current_block.move.assert_called_once_with(0, -1)

    def test_move_right(self):
        game = Game()
        game.current_block = Mock()
        game.block_inside = Mock(return_value=True)
        game.block_fits = Mock(return_value=True)

        game.move_right()

        game.current_block.move.assert_called_once_with(0, 1)

    def test_move_down(self):
        game = Game()
        game.current_block = Mock()
        game.block_inside = Mock(return_value=True)
        game.block_fits = Mock(return_value=True)

        game.move_down()

        game.current_block.move.assert_called_once_with(1, 0)

    def test_lock_block(self):
        game = Game()
        game.current_block = Mock()
        game.next_block = Mock()
        game.get_random_block = Mock(return_value=Mock())
        game.block_fits = Mock(return_value=False)

        game.lock_block()

        game.get_random_block.assert_called_once()
        self.assertEqual(game.game_over, True)

    def test_reset(self):
        game = Game()
        game.get_random_block = Mock(return_value=Mock())

        game.reset()

        game.get_random_block.assert_called_with()

    def test_rotate(self):
        game = Game()
        game.current_block = Mock()
        game.block_inside = Mock(return_value=True)
        game.block_fits = Mock(return_value=True)

        game.rotate()

        game.current_block.rotate.assert_called_once()

    def test_block_inside(self):
        game = Game()
        game.grid.is_inside = Mock(return_value=True)
        game.current_block.get_cell_positions = Mock(return_value=[Mock(), Mock()])

        self.assertEqual(game.block_inside(), True)

    def test_draw(self):
        game = Game()
        game.grid.draw = Mock()
        game.current_block.draw = Mock()
        game.next_block.draw = Mock()

        screen_mock = Mock()
        game.draw(screen_mock)

        game.grid.draw.assert_called_once_with(screen_mock)
        game.current_block.draw.assert_called_once_with(screen_mock, 11, 11)
        game.next_block.draw.assert_called_once_with(screen_mock, 270, 270)


if __name__ == '__main__':
    unittest.main()
