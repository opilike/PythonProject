"""
File: hangman.py
Name:Jason
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    hangman game, check input guess match or not, and have life left
    """
    #  initialize
    num = random_word()
    hint = ''
    life = N_TURNS
    #  make hints
    for i in range(len(num)):
        hint += "-"
    print('The word looks like: '+str(hint))
    #  check if life still have or not !
    while True:
        print('You have ' + str(life) + ' wrong guesses left.')
        print(draw(life))
        answer = input('Your guess: ')
        if answer.isalpha() and len(answer) == 1:
            #  make all input upper !
            answer = answer.upper()
            #  make new_hint be hint
            new_hint = hint
            if answer in num:
                new_hint = make_new_hint(num, hint, answer)
                print('You are correct!')
                #  if win then break
                if new_hint == num:
                    print('You Win!!')
                    print('The answer is: ' + str(num))
                    break
                else:
                    print('The word looks like: ' + str(new_hint))
                #  give return new_hint to hint for loop
                hint = new_hint
            else:
                life -= 1
                print('The is no ' + str(answer) + "'s"' in the word.')
                #  if lose then break
                if life == 0:
                    print('You are completely hung :(')
                    print('The answer is: ' + str(num))
                    print(draw(life))
                    break
                else:
                    print('The word looks like: ' + str(new_hint))
                #  give return new_hint to hint for loop
                hint = new_hint
        else:
            print('Illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def make_new_hint(num, hint, answer):
    new_hint = ''
    for i in range(len(num)):
        ch = num[i]
        if ch == answer:
            new_hint += ch
        else:
            new_hint += hint[i]
    return new_hint


def draw(life):
    """
        Draw hangman !
    """
    life = 7 - life
    if life == 0:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|        |\n"
            "|        -\n"
            "|       - -\n"
            "|        -\n"
            "|\n"      
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 1:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 2:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|        -\n"
            "|        -\n"
            "|        -\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 3:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|        -  -\n"
            "|        -   -\n"
            "|        -\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 4:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|     -  -  -\n"
            "|    -   -   -\n"
            "|        -\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 5:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|     -  -  -\n"
            "|    -   -   -\n"
            "|        -\n"
            "|          -\n"
            "|           -\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 6:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -\n"
            "|     --   --           S\n"
            "|     --   --           O\n"
            "|       - -             S\n"
            "|     -  -  -\n"
            "|    -   -   -\n"
            "|        -\n"
            "|      -  -\n"
            "|     -    -\n"
            "|\n"
            "|\n"
            "----------------"
        )
    elif life == 7:
        return (
            "Your Draw looks like below now:\n"
            "----------------\n"
            "|        |\n"
            "|       - -            YOU\n"    
            "|     -- | --          ARE\n"       
            "|     -- | --          DIED!!\n"
            "|       - -\n"
            "|     -  -  -\n"
            "|    -   -   -\n"
            "|        -\n"
            "|      -  -\n"
            "|     -    -\n"
            "|\n"
            "|\n"
            "----------------"
        )


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
