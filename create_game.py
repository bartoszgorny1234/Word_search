from copy import deepcopy
import numpy as np
from typing import List

from Word_search_board import Word_search_board
from functions import randomrange


def try_to_join(word: str, x: int, y: int, vertical: bool):
    for number in randomrange(0, x - 1):
        for shift in randomrange(0, y - len(word)):
            try:
                game.insert_word(word, vertical, number, shift)
                print(word)
                first_temp_list.pop(0)
                break
            except ValueError:
                print("Eh")

def list_of_longest(words: List, multiplier: float):     #Create list with the longest words.
    num_list = []
    for element in words:                                #Create list with long of words
        num_list.append(len(element))

    temp_list = deepcopy(sorted(words, key=len, reverse=True))    #create sorted copy od words list
    first_temp_list = []
    while len(temp_list[0]) > np.mean(num_list) + multiplier * np.std(num_list):
        first_temp_list.append(temp_list[0])
        temp_list.pop(0)
    return first_temp_list, temp_list


def word_search_game(x: int, y: int, words: List):
    game = Word_search_board(x, y)

    first_temp_list, temp_list = list_of_longest(words, 1)
    game.create_board()
    print(first_temp_list)
    print(temp_list)
    n = 0
    while n < len(words)*100 and first_temp_list != []:
        first_temp_list, temp_list = list_of_longest(words, 1)
        n += 1
        game.create_board()
        word: str = first_temp_list[0]
        pos = list(game.get_random_position(word))
        game.insert_word(word, *pos)
        first_temp_list.pop(0)
        m = 0
        while m < len(temp_list)*1000 and first_temp_list != []:
            m += 1
            word = first_temp_list[0]
            if pos[0]:
                pos[0] = False
                for number in randomrange(0, x-1):
                    for shift in randomrange(0, y-len(word)):
                        pos[1], pos[2] = number, shift
                        try:
                            if word == first_temp_list[0]:
                                game.insert_word(word, *pos)
                                print(word)
                                first_temp_list.pop(0)
                        except ValueError:
                            print("Eh")
                            continue
                break
            else:
                pos[0] = True
                for number in randomrange(0, y):
                    for shift in randomrange(0, x-len(word)):
                        pos[1], pos[2] = number, shift
                        try:
                            if word == first_temp_list[0]:
                                game.insert_word(word, *pos)
                                print(word)
                                first_temp_list.pop(0)
                                break
                        except ValueError:
                            print("Eh2")
    n = 0
    temp_list = first_temp_list + temp_list
    while n < 10000 and temp_list != []:
        n += 1
        try:
            game.insert_word_in_rand(temp_list[0])
            print(temp_list[0])
            temp_list.pop(0)
        except ValueError:
            print(n)
    game.random_letters()
    print(temp_list)
    print(words)
    return game


word_list = ["to",
             "przykładowe",
             "wyrazy",
             "dla",
             "potrzeb",
             "testów",
             "chciałbym",
             "aby",
             "wszystko",
             "zadziałało",
             "jak",
             "powinno",
             "agnostycyzm",
             "agnostyk",
             "agnozja",
             "agonalny",
             "agonia",
             "agonistyczny",
             "agora",
             "agrafia"]

word_list2 = ["mama"]

game = word_search_game(13, 13, word_list)
game.show_board()

