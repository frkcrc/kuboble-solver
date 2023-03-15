import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_parsing(self):
        board_str = '#####\n#...#\n#A.a#\n#####'.split('\n')
        board = Board(board_str)
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
    
    def test_win(self):
        board_str = '#####\n#...#\n#A.a#\n#####'.split('\n')
        board = Board(board_str)
        self.assertTrue(board.is_win((('A', (2,3)),)))
        self.assertFalse(board.is_win((('B', (2,3)),)))
        self.assertFalse(board.is_win((('A', (3,1)),)))
        
        board_str = '#####\n#...#\n#A.a#\n#B.b#\n#####'.split('\n')
        board = Board(board_str)
        self.assertFalse(board.is_win((('A', (2,3)),)))
        self.assertTrue(board.is_win((('A', (2,3)), ('B', (3,3)))))