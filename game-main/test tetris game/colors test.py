import unittest

from colors import Colors  
class TestColors(unittest.TestCase):

    def test_get_cell_colors(self):
        expected_colors = [
            (26, 31, 40),  # dark_grey
            (47, 230, 23),  # green
            (232, 18, 18),  # red
            (226, 116, 17),  # orange
            (237, 234, 4),  # yellow
            (166, 0, 247),  # purple
            (21, 204, 209),  # cyan
            (13, 64, 216)  # blue
        ]
        colors = Colors.get_cell_colors()
        self.assertEqual(len(colors), len(expected_colors))
        for color, expected_color in zip(colors, expected_colors):
            self.assertEqual(color, expected_color)


if __name__ == '__main__':
    unittest.main()
