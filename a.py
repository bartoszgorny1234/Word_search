class WordSearch:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._board = []

    def create_board(self):
        empty_list = []
        for num in range(0, self._x):
            empty_list.append(num)
        for num2 in range(0, self._y):
            self._board.append(empty_list)

    def show_board(self):
        for row in self._board:
            print(row)

    def get_line(self, vertical: bool, number: int) -> str:
        line = []
        if vertical:
            for row in self._board:
                line.append(row[number])
        else:
            line = self._board[number]
        return line

    def get_random_word(self, word: str) -> str:
        return word







# Tutaj sobie testuje różne funkcjonalności
test = WordSearch(4, 5)
# test_get_line = Anagram(4,5)

test.create_board()
test.show_board()
# test.insert_word("mama")
print("\n")
print(test.get_line(True, 3))
print("\n")
print(test.get_line(False, 1))