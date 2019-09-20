import random


class WordSearch:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._board = []

    def create_my_board(self):
        for _ in range(0, self._x * self._y):
            self._board.append('')
        print(f'This is my board: {self._board}')

    def show_board(self):
        n = 0
        for _ in range(0, self._y):
            print(self._board[self._x * n: self._x * (n + 1)])
            n += 1

    def test_word(self):
        n = 0
        testword = 'mama'
        for e in testword:
            self._board[0 + n] = e
            n += 1

    def add_random_word(self):
        # losuję pion lub poziom
        horizontal = random.choice([True, False])

        # losuję lokalizację początkowej litery
        # sprawdz czy nie wylosuje mi tutaj za dużej liczby - może jakiś test?
        word_starts_at = random.randrange(0, self._x * self._y - 2, 1)

        if horizontal:
            print(f'horizontal word starts at {word_starts_at}')
            if word_starts_at % self._x+1:
                print('You cannot put your horizontal word here')
            else:
                print('You can put your horizontal word here')

        else:
            word_starts_at = random.randrange(0, self._x * self._y - 2, 1)
            print(f'vartical word starts at {word_starts_at}')




new_board_test = WordSearch(4, 5)
# tworzę pustą tablicę
new_board_test.create_my_board()

print('Printuję pustą tablicę')
new_board_test.show_board()

# dodaję testowe słowo do tablicy
new_board_test.test_word()

# printuję zmienioną tablicę
print('Printuję zmienioną tablicę')
new_board_test.show_board()

print('Adding random word')
new_board_test.add_random_word()

