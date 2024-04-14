import unittest
from position import Position  

class TestPosition(unittest.TestCase):

    def test_init(self):
        row = 2
        column = 3
        position = Position(row, column)

        self.assertEqual(position.row, row)
        self.assertEqual(position.column, column)


if __name__ == '__main__':
    unittest.main()
