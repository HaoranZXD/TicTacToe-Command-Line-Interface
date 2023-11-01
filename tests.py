import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def other_player(self):
        player = "X"
        self.assertEqual(logic.other_player(player), "O")


if __name__ == '__main__':
    unittest.main()
