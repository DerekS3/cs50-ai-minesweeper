import unittest
from minesweeper import *


# Test Sentence 
class TestKnownMines(unittest.TestCase):
    def setUp(self):
        cells = {(0, 0), (0, 1), (1, 0)}
        count = 2
        self.sentence = Sentence(cells, count)

    def test_mines_on_all_cells(self):
        # All cells are known mines when count equals number of cells
        self.sentence.count = 3
        expected_result = self.sentence.cells
        self.assertEqual(self.sentence.known_mines(), expected_result)
    
    def test_unknown_mine_location(self):
        # When number of cells not equal to count, mine location is unknown
        expected_result = set()
        self.assertEqual(self.sentence.known_mines(), expected_result)


class TestKnownSafes(unittest.TestCase):
    def setUp(self):
        cells = {(0, 0), (0, 1), (1, 0)}
        count = 2
        self.sentence = Sentence(cells, count)

    def test_all_cells_safe(self):
        # All cells are known safe when count equals 0
        self.sentence.count = 0
        expected_result = self.sentence.cells
        self.assertEqual(self.sentence.known_safes(), expected_result)
    
    def test_unknown_safe_location(self):
        # When number of cells not equal to count, safe location is unknown
        expected_result = set()
        self.assertEqual(self.sentence.known_safes(), expected_result)


class TestMarkMine(unittest.TestCase):
    def setUp(self):
        cells = {(0, 0), (0, 1), (1, 0)}
        count = 2
        self.sentence = Sentence(cells, count)
    
    def test_mark_cell_as_mine(self):
        mine = (1, 0) 
        expected_cells = {(0, 0), (0, 1)}
        expected_count = 1
        self.sentence.mark_mine(mine)
        self.assertEqual(self.sentence.cells, expected_cells)
        self.assertEqual(self.sentence.count, expected_count)

    def test_mine_cell_not_in_sentence(self):
        mine = (1, 1)
        expected_result = self.sentence.cells
        self.sentence.mark_mine(mine)
        self.assertEqual(self.sentence.cells, expected_result)


class TestMarkSafe(unittest.TestCase):
    def setUp(self):
        cells = {(0, 0), (0, 1), (1, 0)}
        count = 2
        self.sentence = Sentence(cells, count)

    def test_mark_cell_as_safe(self):
        safe = (1, 0)
        expected_result = {(0, 0), (0, 1)}
        self.sentence.mark_safe(safe)
        self.assertEqual(self.sentence.cells, expected_result)

    def test_safe_cell_not_in_sentence(self):
        safe = (1, 1)
        expected_result = self.sentence.cells
        self.sentence.mark_safe(safe)
        self.assertEqual(self.sentence.cells, expected_result)


# Test MinsweeperAI
class TestAddKnowledge(unittest.TestCase):
    def setUp(self):
        self.ai = MinesweeperAI()
        self.ai.add_knowledge((0, 1), 1)

    def test_add_knowledge(self):
        self.assertIsInstance(self.ai.knowledge[0], Sentence)


class TestMakeSafeMove(unittest.TestCase):
    def setUp(self):
        self.ai = MinesweeperAI()

    def test_make_safe_move(self):
        safe_cell = (1, 1)
        self.ai.mark_safe(safe_cell)
        self.assertEqual(self.ai.make_safe_move(), safe_cell)
        

class TestMakeRandomMove(unittest.TestCase):
    def setUp(self):
        self.ai = MinesweeperAI()

    def test_make_random_move(self):
        # Check all possible moves appear in a sample of 500
        moves = set(self.ai.make_random_move() for i in range(500))
        expected_result = self.ai.width * self.ai.height
        self.assertEqual(len(moves), expected_result)


if __name__ == '__main__':
    unittest.main()