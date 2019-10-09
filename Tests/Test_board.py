import unittest
from unittest.mock import MagicMock, patch
from Word_search_board import Word_search_board

word_list = ["agar",
             "agencja",
             "agencyjny",
             "agenda",
             "agenturalny",
             "agentura",
             "agitacja",
             "agitka",
             "agitować",
             "aglomeracja",
             "aglomerować",
             "aglutynacja",
             "agnostycyzm",
             "agnostyk",
             "agnozja",
             "agonalny",
             "agonia",
             "agonistyczny",
             "agora",
             "agrafia"]

word_list2 = ["mama", "tata"]

class Test_class(unittest.TestCase):
    def setUp(self):                                #przy każdym teście resetuje wartości wejściowe
        print("SetUpTest")
        self.board1 = Word_search_board(4, 4)
        self.board2 = Word_search_board(12, 10)
        self.board1.create_board()
        self.board2.create_board()

    def tearDown(self):
        print("TearDown")

    def test_01_create_board(self):
        print("01 CREATE BOARD")
        self.assertEqual(self.board1._board,    [["*", "*", "*", "*"],
                                                ["*", "*", "*", "*"],
                                                ["*", "*", "*", "*"],
                                                ["*", "*", "*", "*"]])

        self.assertEqual(self.board2._board, [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                             ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]])

    def test_02_1_check_line(self):
        print("02_1 check line")
        self.assertIsNone(self.board1.check_line(True, 0))
        self.assertIsNone(self.board1.check_line(False, 0))
        self.assertIsNone(self.board1.check_line(True, 3))
        self.assertIsNone(self.board1.check_line(False, 3))
        self.assertIsNone(self.board2.check_line(True, 0))
        self.assertIsNone(self.board2.check_line(False, 0))
        self.assertIsNone(self.board2.check_line(True, 9))
        self.assertIsNone(self.board2.check_line(False, 11))


    def test_02_2_check_line(self):
        print("02_2 check line but ValueError")
        with self.assertRaises(ValueError):
            self.board1.check_line(True, 4)
        with self.assertRaises(ValueError):
            self.board1.check_line(False, 4)
        with self.assertRaises(ValueError):
            self.board1.check_line(True, -1)
        with self.assertRaises(ValueError):
            self.board1.check_line(False, -1)
        with self.assertRaises(ValueError):
            self.board2.check_line(True, 10)
        with self.assertRaises(ValueError):
            self.board2.check_line(False, 12)
        with self.assertRaises(ValueError):
            self.board2.check_line(True, -1)
        with self.assertRaises(ValueError):
            self.board2.check_line(False, -1)

    def test_03_1_check_word(self):
        print("03_1 check word")
        self.assertIsNone(self.board1.check_word(["M", "A", "M", "A"], True, 0, 0))
        self.assertIsNone(self.board1.check_word(["M", "A", "M", "A"], False, 3, 0))
        self.assertIsNone(self.board1.check_word(["M", "A"], True, 0, 2))
        self.assertIsNone(self.board1.check_word(["M", "A"], False, 3, 2))
        self.assertIsNone(self.board2.check_word(["M", "A", "M", "A", "M", "A", "M", "A", "M", "A"], True, 0, 0))
        self.assertIsNone(self.board2.check_word(["M", "A", "M", "A", "M", "A", "M", "A", "M", "A", "M", "A"], False, 0, 0))
        self.assertIsNone(self.board2.check_word(["M", "A"], True, 0, 8))
        self.assertIsNone(self.board2.check_word(["M", "A"], False, 0, 10))

    def test_03_2_check_word(self):
        print("03_2 check word but value error")
        with self.assertRaises(ValueError):
            self.board1.check_word(["M", "A", "M", "A", "M"], True, 0, 0)
        with self.assertRaises(ValueError):
            self.board1.check_word(["M", "A", "M", "A", "M"], False, 3, 0)
        with self.assertRaises(ValueError):
            self.board1.check_word(["M", "A"], True, 0, 3)
        with self.assertRaises(ValueError):
            self.board1.check_word(["M", "A"], False, 3, 3)
        with self.assertRaises(ValueError):
            self.board2.check_word(["M", "A", "M", "A", "M", "A", "M", "A", "M", "A", "M"], True, 0, 0)
        with self.assertRaises(ValueError):
            self.board2.check_word(["M", "A", "M", "A", "M", "A", "M", "A", "M", "A", "M", "A", "M"], False, 0, 0)
        with self.assertRaises(ValueError):
            self.board2.check_word(["M", "A"], True, 0, 9)
        with self.assertRaises(ValueError):
            self.board2.check_word(["M", "A"], False, 0, 11)

    def test_04_insert_word(self):
        print("04_1 insert word")
        self.assertIsNone(self.board1.insert_word("MAMA", True, 0, 0))
        self.assertIsNone(self.board1.insert_word("MAMA", False, 2, 0))
        self.assertIsNone(self.board1.insert_word("MA", True, 2, 2))
        self.assertIsNone(self.board1.insert_word("MA", False, 0, 2))

        self.assertIsNone(self.board2.insert_word("MAMAMAMAMA", True, 0, 0))
        self.assertIsNone(self.board2.insert_word("MAMAMAMAMAMA", False, 0, 0))
        self.assertIsNone(self.board2.insert_word("MA", True, 2, 8))
        self.assertIsNone(self.board2.insert_word("MA", False, 2, 10))


    def test_04_2_insert_word(self):
        print("04_2 insert word with error")
        with self.assertRaises(ValueError):
            self.board1.insert_word("MAMAMA", True, 0, 0)
        with self.assertRaises(ValueError):
            self.board1.insert_word("MAMAMA", False, 3, 0)
        with self.assertRaises(ValueError):
            self.board1.insert_word("MA", True, 0, 3)
        with self.assertRaises(ValueError):
            self.board1.insert_word("MA", False, 3, 3)

        self.board1.insert_word("MAMA", False, 2, 0)
        self.board1.insert_word("MAMA", True, 0, 0)
        with self.assertRaises(ValueError):
            self.board1.insert_word("MA", False, 1, 0)
        with self.assertRaises(ValueError):
            self.board1.insert_word("MA", True, 2, 1)

        with self.assertRaises(ValueError):
            self.board2.insert_word("MAMAMAMAMAMA", True, 0, 0)
        with self.assertRaises(ValueError):
            self.board2.insert_word("MAMAMAMAMAMAM", False, 0, 0)
        with self.assertRaises(ValueError):
            self.board2.insert_word("MA", True, 0, 9)
        with self.assertRaises(ValueError):
            self.board2.insert_word("MA", False, 0, 11)

    def test_05_randomposition(self):
        print("05_random_position")
        for _ in range(0, 100):
            pos = self.board1.get_random_position("MA")
            if pos[0]:
                self.assertLess(pos[1], 4)
                self.assertLess(pos[2], 2)
            else:
                self.assertLess(pos[1], 4)
                self.assertLess(pos[2], 2)
        for _ in range(0, 100):
            pos = self.board2.get_random_position("MA")
            if pos[0]:
                self.assertGreaterEqual(pos[1], 0)
                self.assertGreaterEqual(pos[2], 0)
                self.assertLess(pos[1], 12)
                self.assertLess(pos[2], 8)
            else:
                self.assertGreaterEqual(pos[1], 0)
                self.assertGreaterEqual(pos[2], 0)
                self.assertLess(pos[1], 10)
                self.assertLess(pos[2], 10)
