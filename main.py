    # -*- coding: utf-8 -*-
# Python version 2.7 required
import math
import random

# Init global variables

# Count tries
count = 0

# Secren random number for range
secret = 0


# Handlers


def dif_level(player_input):
    """Customizable difficulty"""
    if player_input in range(1, 1001):
        return player_input
    else:
        print "ERROR! RANGE ONLY 1 - 1000"
        exit(1)


def max_range_of_game_f(str):
    """Max range of number"""
    max_range = str * 100
    return max_range


def num_of_try(max_range):
    """Numbers of tries. Player always may win"""
    return int(math.ceil(math.log(max_range, 2)))


def secret_number(str):
    """Create secret number"""
    return int(random.randrange(1, str + 1))


def reset_end_begin():
    print "Wanna play one more time? =)"
    answer = raw_input("> (yes, no) >>> ")
    if answer == "yes":
        print "Okay... Let's do it again."
        start()
    elif answer == "no":
        print "Sad.. Good Bye!"
        exit(1)
    else:
        print "What you say? Yes or No? (You may press Ctrl+D for exit app)"
        reset_end_begin()


# Start


def start():

    global difficult
    global max_range_of_game
    global count
    global secret

    print """
                 Let's play a GAME!

                  ==          ==
                   ==        ==

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

    print """Choose number in range 1 - 1000. It will be difficult level.
    (Ex: 1 - easy. 1000 - hard)"""

    difficult = dif_level(int(raw_input()))

    max_range_of_game = max_range_of_game_f(difficult)

    print "Play in range from 1 to %d" % max_range_of_game

    count = num_of_try(max_range_of_game)

    print "Tries: %d" % count

    print "Guessing number. Magic..."

    secret = secret_number(max_range_of_game)

    # print "Ты этого не видел %d" % secret

    print "Okay. Let's do it. What's the number in my head?"

    try_to_guess()


def try_to_guess():
    global count
    player_try = int(raw_input("> "))
    if player_try == secret and count >= 1:
        print "WoW! You Win! It's really %s" % secret
        raw_input("> Press RETURN to continue")
        reset_end_begin()

    elif player_try > secret and count > 1:
        count -= 1
        print "No. LESS. %d tries left." % count
        try_to_guess()

    elif player_try < secret and count > 1:
        count -= 1
        print "No. GREATER.%d tries left" % count
        try_to_guess()

    elif count <= 1:
        print """Oh.. You Lose. Right answer was: %s.
        Maybe in another game you will be lucky! =)""" % secret
        reset_end_begin()

    else:
        print "OH. IT'S BIG ERROR. SORRY."
        exit(1)

start()
