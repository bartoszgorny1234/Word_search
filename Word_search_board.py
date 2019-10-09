from typing import List
from string import ascii_letters
from random import random, randint, choice


class Word_search_board:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._board = []

    def create_board(self):
        self._board = []
        for _ in range(0, self._y):
            empty_list = []
            for _ in range(0, self._x):
                empty_list.append("*")
            self._board.append(empty_list)

    def show_board(self):
        for row in self._board:
            print(row)

    def check_line(self, vertical: bool, number: int):
        if vertical:
            if number >= self._y or number < 0:
                raise ValueError
        else:
            if number >= self._x or number < 0:
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

    def get_random_position(self, word: str):
        len_word = len(word)
        vertical = random() < 0.5
        if vertical:
            num = randint(0, self._x-1)
            shift = randint(0, (self._y-len_word-1))
        else:
            num = randint(0, self._y-1)
            shift = randint(0, (self._x-len_word-1))
        return vertical, num, shift

    def check_word(self, word: List, vertical: bool, number: int, shift: int):
        line = self.get_line(vertical, number)
        if (len(word)+shift) > len(line):
            raise ValueError
        else:
            for num in range(0, len(word)):
                if line[num+shift] != "*" and word[num] != line[num+shift]:
                    raise ValueError

    def insert_word(self, word: str, vertical: bool, number: int, shift: int):
        word = list(word.upper())
        try:
            self.check_word(word, vertical, number, shift)
            for num, letter in enumerate(word, 0):
                if vertical:
                    self._board[num+shift][number] = letter
                else:
                    self._board[number][num+shift] = letter
        except ValueError:
            raise ValueError

    def insert_word_in_rand(self, word: str):
        pos = self.get_random_position(word)
        self.insert_word(word, *pos)

    def random_letters(self):
        for x in range(0, self._x):
            for y in range(0, self._y):
                if self._board[y][x] == "*":
                    self._board[y][x] = choice(ascii_letters.upper())



# word_list = ["agar"]
# game = Word_search_board(4, 4)
# game.create_board()
# game.show_board()
# word = word_list[0]
# print(word)
# position = game.get_random_position(word)
# game.insert_word(*position, word)
# game.show_board()