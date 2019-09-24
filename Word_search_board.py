from string import ascii_letters
from random import random, randint, choice


class Word_search_board:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._board = []

    def create_board(self):
        n=0
        for _ in range(0, self._y):
            empty_list = []
            for _ in range(0, self._x):
                empty_list.append("")
                n += 1
            self._board.append(empty_list)

    def show_board(self):
        for row in self._board:
            print(row)

    def check_line(self, vertical: bool, number: int):
        if vertical:
            if number >= self._x:
                raise ValueError
        else:
            if number >= self._y:
                raise ValueError


    def get_line(self, vertical: bool, number: int) -> list:
        self.check_line(vertical, number)
        line = []
        if vertical:
            for num in range(0, self._y):
                line.append(self._board[num][number])
        else:
            line = self._board[number]
        return line

    def get_random_line(self):
        vertical = random() < 0.5
        if vertical:
            num = randint(0, self._x-1)
        else:
            num = randint(0, self._y-1)
        return self.get_line(vertical, num)

    def insert_word(self, vertical: bool, number: int, word: str):
        word = list(word.upper())
        for num, letter in enumerate(word, 0):
            if vertical:
                self._board[num][number] = letter
            else:
                self._board[number][num] = letter

    def random_letters(self):
        for x in range(0, self._x):
            for y in range(0, self._y):
                if self._board[y][x] == "":
                    self._board[y][x] = choice(ascii_letters.upper())

# Tutaj sobie testuje różne funkcjonalności
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
print(word_list[0:10:2])
test = Word_search_board(4, 5)

test.create_board()
test.show_board()
print("\n"*2)
test.check_line(False, 4)
print(test.get_line(True, 3)) #min0 max3
print(test.get_line(False, 4)) #min0 max4
print("\n"*2)
print(test.get_random_line())
print(test.get_random_line())
print(test.get_random_line())
print("\n"*2)
test.insert_word(False, 1, "tata")
test.insert_word(True, 1, "mAma")
test.show_board()
print("\n"*2)
test.random_letters()
test.show_board()