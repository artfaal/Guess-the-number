# -*- coding: utf-8 -*-
# Давайте попробуем еще раз
import math
import random

# Инициализируем Глобальные Переменные

count = 0
secret = 0

# Обработчики

def dif_level(player_input):
    """Определяем уровень сложности"""
    if player_input in range(1, 1001):
        return player_input
    else:
        print "ERROR! RANGE ONLY 1 - 1001"
        exit(1)


def max_range_of_game_f(str):
    """Определяем, какой будет макс рейндж."""
    max_range = str * 100
    return max_range


def num_of_try(max_range):
    """Количество попыток"""
    return int(math.ceil(math.log(max_range, 2)))


def secret_number(str):
    """Загадываем число"""
    return int(random.randrange(1, str + 1))


def reset_end_begin():
    print "Хочешь сыграть еще?"
    answer = raw_input("yes or no > ")
    if answer == ("yes" or "Yes"):
        print "Ну давай сыграем еще раз..."
        start()
    elif answer == ("no" or "No"):
        print "Жаль.. Ну тогда пока.."
        exit(1)
    else:
        print "What you say? Yes or No? (You may press Ctrl+D for exit app)"
        reset_end_begin()

# Экшн

def start():

    global difficult, max_range_of_game, count, secret

    print """
                 Let's play a GAME!

                  ==          ==
                   ==        ==
                     ==     ==
                    ==       ==
                    ==       ==
                    ==       ==
                    ==       ==
            ===     ==       ==     ===
             ===    ==       ==    ===
              ===   ==       ==   ===
               ===  ==       ==  ===
                ===             ===
                  ====       ====
                    ============
                      =======
"""

    print "Выбери в диапазоне от 1 до 1000. Это задаст сложность игры."

    difficult = dif_level(int(raw_input()))

    max_range_of_game = max_range_of_game_f(difficult)

    print "Играем в диапазоне чисел от 1 до %d" % max_range_of_game

    count = num_of_try(max_range_of_game)

    print "Колчество попыток: %d" % count

    print "Загадываю число........ "

    secret = secret_number(max_range_of_game)

    # print "Ты этого не видел %d" % secret

    print "Ну, жги. Какое число?"

    try_to_gues()

def try_to_gues():
    global count
    player_try = int(raw_input("> "))
    if player_try == secret and count >= 1:
        print "ВСЁ! НАХРЕН ПОБЕДИЛ ВСЕХ БЛИН!!! ТЮТЮТЮЮЮЮЮ!!!!!"
        raw_input("RETURN to continue")
        reset_end_begin()


    elif player_try > secret and count > 1 :
        count -= 1
        print "Загаданное меньше. Осталось %d попыток" % count
        try_to_gues()

    elif player_try < secret and count > 1:
        count -= 1
        print "Загаданное больше. Осталось %d попыток" % count
        try_to_gues()

    elif count <= 1:
        print "Ну всё, жопень. Проиграл ты, пацанчик."
        reset_end_begin()

    else:
        print "ПИЗДЕЦ! НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ!"
        exit(1)

start()
