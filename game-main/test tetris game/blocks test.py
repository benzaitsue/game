import unittest
from unittest.mock import patch, Mock

from blocks import LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock  

class TestBlocks(unittest.TestCase):

    def test_l_block_init(self):
        l_block = LBlock()
        self.assertEqual(l_block.id, 1)
        self.assertEqual(l_block.row_offset, 0)
        self.assertEqual(l_block.column_offset, 3)

    def test_j_block_init(self):
        j_block = JBlock()
        self.assertEqual(j_block.id, 2)
        self.assertEqual(j_block.row_offset, 0)
        self.assertEqual(j_block.column_offset, 3)

    def test_i_block_init(self):
        i_block = IBlock()
        self.assertEqual(i_block.id, 3)
        self.assertEqual(i_block.row_offset, -1)
        self.assertEqual(i_block.column_offset, 3)

    def test_o_block_init(self):
        o_block = OBlock()
        self.assertEqual(o_block.id, 4)
        self.assertEqual(o_block.row_offset, 0)
        self.assertEqual(o_block.column_offset, 4)

    def test_s_block_init(self):
        s_block = SBlock()
        self.assertEqual(s_block.id, 5)
        self.assertEqual(s_block.row_offset, 0)
        self.assertEqual(s_block.column_offset, 3)

    def test_t_block_init(self):
        t_block = TBlock()
        self.assertEqual(t_block.id, 6)
        self.assertEqual(t_block.row_offset, 0)
        self.assertEqual(t_block.column_offset, 3)

    def test_z_block_init(self):
        z_block = ZBlock()
        self.assertEqual(z_block.id, 7)
        self.assertEqual(z_block.row_offset, 0)
        self.assertEqual(z_block.column_offset, 3)


if __name__ == '__main__':
    unittest.main()
