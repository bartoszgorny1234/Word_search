import random


class WordSearch:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._board = []

    def create_my_board(self):
        for _ in range(0, self._x * self._y):
            self._board.append('')
        print(f'This is my board: {self._board}\n')

    def show_board(self):
        n = 0
        for _ in range(0, self._y):
            print(self._board[self._x * n: self._x * (n + 1)])
            n += 1

    # def test_word(self):
    #     n = 0
    #     testword = 'mama'
    #     for e in testword:
    #         self._board[0 + n] = e
    #         n += 1

    def word_start_position(self):
        # losuję lokalizację początkowej litery
        word_starts_at = random.randrange(0, self._x * self._y - 1, 1)
        print(f"\n1. Wylosowałem lokalizację początkowej litery: {word_starts_at}")
        input("                 Press Enter to continue...")

        # losuję pion lub poziom
        horizontal = random.choice([True, False])
        print(f'\n2. Horizontal [True/False]: {horizontal}')
        input("                 Press Enter to continue...")

        # checking if its possible to add word with minimum 2 letters:
        if horizontal:
            # checking if possible to put two-letter-word horizontal here
            print(f'\n3. Word starts at position: {word_starts_at}, as horizontal.')
            if word_starts_at % self._x == word_starts_at - 1:
                print('\nYou cannot put your horizontal word here. Only one letter word match here.')
                input("                 Press Enter to continue...")
                new_board_test.word_start_position()  # chwilowo, potem ogramy ogólnym programem
            else:
                print('You can put your horizontal word here.')
                # new_board_test.match_word_to_position(horizontal, word_starts_at)
                new_board_test.max_word_lenght(horizontal, word_starts_at)
        else:
            # checking if possible to add minimum two-letter vertical word here
            print(f'\n3. Word starts at position: {word_starts_at}, as vertical.')
            if word_starts_at % self._y == word_starts_at - 1:
                print('\nYou cannot put your vertical word here . Only one letter word match here.')
                input("                     Press Enter to continue...")
                new_board_test.word_start_position()
            else:
                print('You can put your vertical word here.')
                # new_board_test.match_word_to_position(horizontal, word_starts_at)
                new_board_test.max_word_lenght(horizontal, word_starts_at)

    def max_word_lenght(self, vector: bool, position: int) -> int:
        print(vector)
        if vector:
            max_word_lenght = self._x - (position % self._x)
            print(f'\nMax word lenght is {max_word_lenght}.')
            input("                     Press Enter to continue...")

        else:
            max_word_lenght = int(self._x - (position / self._x)) + 1
            print(f'\nMax word lenght is {max_word_lenght}.')
            input("                     Press Enter to continue...")

        new_board_test.draw_word(max_word_lenght)


    def draw_word(self, max_wod_lenght):

        print('drawing word')



    def match_word_to_position(self, vector: bool, position, word='ul'):  # position
        n = 0  # zmienna pomocniczna
        m = self._x  # zmienna pomocnicza
        print(position)
        print(vector)
        if vector:
            for horizontal_letter in word:
                self._board[position + n] = horizontal_letter
                n += 1
        else:
            for vertical_letter in word:
                self._board[position + m] = vertical_letter
                m += self._x
        self.show_board()


# zrob testy


new_board_test = WordSearch(4, 4)

new_board_test.create_my_board()

new_board_test.show_board()

# new_board_test.test_word()

new_board_test.word_start_position()
input("                 Press Enter to continue...")

# new_board_test.show_board()
