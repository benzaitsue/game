import unittest
import pygame
from unittest.mock import patch, Mock

from main import main 

class TestMain(unittest.TestCase):

    @patch('pygame.quit')
    @patch('sys.exit')
    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    @patch('pygame.time.Clock')
    @patch('pygame.time.set_timer')
    @patch('pygame.event.get')
    def test_main(self, mock_event_get, mock_set_timer, mock_clock, mock_display_set_mode,
                  mock_init, mock_exit, mock_quit):
        pygame_mock = Mock()
        pygame_mock.USEREVENT = 1
        pygame_mock.KEYDOWN = 2
        pygame_mock.K_LEFT = 3
        pygame_mock.K_RIGHT = 4
        pygame_mock.K_DOWN = 5
        pygame_mock.K_UP = 6
        pygame_mock.QUIT = 7
        pygame_mock.time.set_timer.side_effect = None
        pygame_mock.time.Clock.return_value = Mock()
        mock_event_get.side_effect = [
            [pygame_mock.event.Event(pygame_mock.QUIT)],
            [pygame_mock.event.Event(pygame_mock.KEYDOWN, {'key': pygame_mock.K_LEFT})],
            [pygame_mock.event.Event(pygame_mock.KEYDOWN, {'key': pygame_mock.K_RIGHT})],
            [pygame_mock.event.Event(pygame_mock.KEYDOWN, {'key': pygame_mock.K_DOWN})],
            [pygame_mock.event.Event(pygame_mock.KEYDOWN, {'key': pygame_mock.K_UP})],
            [pygame_mock.event.Event(pygame_mock.USEREVENT)],
            [pygame_mock.event.Event(pygame_mock.QUIT)]
        ]
        mock_display_set_mode.return_value = Mock()
        mock_set_timer.return_value = None
        mock_init.return_value = None
        main()
        mock_quit.assert_called_once()
        mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
