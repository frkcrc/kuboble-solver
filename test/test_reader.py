import unittest
from board import Board
from reader import read

class TestReader(unittest.TestCase):

    def test_read(self):
        kuboble_str = '1\nA,2,1,2,3\n#####\n#...#\n#...#\n#####'
        moves, board = read(kuboble_str)
        self.assertEqual(moves, 1)
        self.assertEqual(board._board, 
          [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]
        )
        self.assertEqual(board._n, 4)
        self.assertEqual(board._m, 5)
        self.assertIn('A', board._starts)
        self.assertIn('A', board._targets)
        self.assertEqual(board._starts['A'], (2,1))
        self.assertEqual(board._targets['A'], (2,3))
        self.assertEqual(board.get_start(), (('A', (2,1)),))