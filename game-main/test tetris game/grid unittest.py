import unittest
from unittest.mock import patch, Mock

from grid import Grid  


class TestGrid(unittest.TestCase):

    def test_is_inside(self):
        grid = Grid()

        self.assertTrue(grid.is_inside(0, 0))
        self.assertTrue(grid.is_inside(19, 9))
        self.assertFalse(grid.is_inside(-1, 0))
        self.assertFalse(grid.is_inside(0, 10))
        self.assertFalse(grid.is_inside(20, 9))
        self.assertFalse(grid.is_inside(19, 10))

    def test_is_empty(self):
        grid = Grid()
        grid.grid[0][0] = 1

        self.assertFalse(grid.is_empty(0, 0))
        self.assertTrue(grid.is_empty(1, 1))

    def test_is_row_full(self):
        grid = Grid()
        grid.grid[0] = [1] * grid.num_cols

        self.assertTrue(grid.is_row_full(0))
        self.assertFalse(grid.is_row_full(1))

    def test_clear_row(self):
        grid = Grid()
        grid.grid[0] = [1] * grid.num_cols

        grid.clear_row(0)

        self.assertEqual(grid.grid[0], [0] * grid.num_cols)

    def test_move_row_down(self):
        grid = Grid()
        grid.grid[0] = [1] * grid.num_cols

        grid.move_row_down(0, 2)

        self.assertEqual(grid.grid[2], [1] * grid.num_cols)
        self.assertEqual(grid.grid[0], [0] * grid.num_cols)

    def test_clear_full_rows(self):
        grid = Grid()
        grid.grid[0] = [1] * grid.num_cols

        completed = grid.clear_full_rows()

        self.assertEqual(completed, 1)
        self.assertEqual(grid.grid[0], [0] * grid.num_cols)

    def test_reset(self):
        grid = Grid()
        grid.grid[0] = [1] * grid.num_cols

        grid.reset()

        self.assertEqual(grid.grid, [[0] * grid.num_cols for _ in range(grid.num_rows)])

    def test_draw(self):
        pygame_mock = Mock()
        pygame_mock.Rect.return_value = Mock()
        pygame_mock.draw.rect = Mock()
        screen_mock = Mock()
        grid = Grid()

        grid.draw(screen_mock)

        for row in range(grid.num_rows):
            for column in range(grid.num_cols):
                cell_value = grid.grid[row][column]
                cell_rect = pygame_mock.Rect.return_value
                pygame_mock.Rect.assert_called_with(column*grid.cell_size + 11, row*grid.cell_size + 11,
                                                     grid.cell_size - 1, grid.cell_size - 1)
                pygame_mock.draw.rect.assert_called_with(screen_mock, grid.colors[cell_value], cell_rect)


if __name__ == '__main__':
    unittest.main()
