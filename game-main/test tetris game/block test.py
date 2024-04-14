import unittest
from unittest.mock import patch, Mock

from block import block 


class TestBlock(unittest.TestCase):

    def test_move(self):
        # Create an instance of Block
        block = block(id=0)

        # Call the move method
        block.move(rows=1, columns=2)

        # Assert that row_offset and column_offset are updated
        self.assertEqual(block.row_offset, 1)
        self.assertEqual(block.column_offset, 2)

    def test_get_cell_positions(self):
        # Create an instance of block
        block = block(id=0)
        block.cells = {0: [Mock(row=0, column=0), Mock(row=1, column=1)]}

        # Call the get_cell_positions method
        positions = block.get_cell_positions()

        # Assert that the positions are correctly adjusted
        self.assertEqual(len(positions), 2)
        self.assertEqual(positions[0].row, 0)
        self.assertEqual(positions[0].column, 0)
        self.assertEqual(positions[1].row, 1)
        self.assertEqual(positions[1].column, 1)

    @patch('block.Colors')
    def test_draw(self, mock_colors):
        # Create an instance of Block
        block = block(id=0)

        # Mock the get_cell_colors method of Colors class
        mock_colors_instance = mock_colors.return_value
        mock_colors_instance.get_cell_colors.return_value = {0: (255, 0, 0)}  # Mocked colors

        # Mock get_cell_positions method
        block.get_cell_positions = Mock(return_value=[Mock(row=0, column=0)])

        # Mock draw method of pygame
        mock_pygame_draw = Mock()
        with patch('block.pygame.draw', mock_pygame_draw):
            # Call the draw method
            block.draw(screen=Mock(), offset_x=0, offset_y=0)

        # Assert that pygame.draw.rect was called
        mock_pygame_draw.rect.assert_called_once()


if __name__ == '__main__':
    unittest.main()
