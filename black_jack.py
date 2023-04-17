import random
import pyfiglet
import time
import os

CARDS_SCORE = {'ace': 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}
CARDS_NAMES = ['ace', '1', '2', '3', '4', '5', '6',
               '7', '8', '9', '10', 'jack', 'queen', 'king']


def Main():
    """
    Take user inputs. Nothing return.
    """
    os.system('clear')
    while True:
        print("""
+-------------------------------------------------------+  
|    ____  _            _          _            _       |
|   | __ )| | __ _  ___| | __     | | __ _  ___| | __   |
|   |  _ \| |/ _` |/ __| |/ /  _  | |/ _` |/ __| |/ /   |
|   | |_) | | (_| | (__|   <  | |_| | (_| | (__|   <    |
|   |____/|_|\__,_|\___|_|\_\  \___/ \__,_|\___|_|\_\\   |
|                                                       |
|                  Online Python Casino                 |
+-------------------------------------------------------+
    """)
        user_name_input = input(
            'Insert your nick (nick must be longer than 1 character): ')
        if len(user_name_input) > 1:
            user_answer_input = input(
                f'{user_name_input}, do you know the rules of BlackJack? (Y)yes or (N)no?: ').lower()
            if user_answer_input == 'y':
                game_core()
            elif user_answer_input == 'n':
                rules_hud()
            else:
                print('Input error! Try again')
                time.sleep(0.5)
                os.system('clear')
        else:
            print('Input error! Try again')
            time.sleep(0.5)
            os.system('clear')
        break


def rules_hud():
    """"
    Open reules page. Nothing return.
    """
    while True:
        print("""
    +---------------------------------------------------------------------------------------------------------------+
    |                                                                                                               |
    |                                                   RULES                                                       |
    |   Blackjack hands are scored by their point total.                                                            |
    |   The hand with the highest total wins as long as it doesn't exceed 21;                                       |
    |   a hand with a higher total than 21 is said to bust.                                                         |
    |   Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10.        |
    |   An ace's value is 11 unless this would cause the player to bust, in which case it is worth 1.               |
    |   A hand in which an ace's value is counted as 11 is called a soft hand,                                      |
    |   because it cannot be busted if the player draws another card.                                               |
    |   The goal of each player is to beat the dealer by having the higher,                                         |
    |   unbusted hand. Note that if the player busts he loses,                                                      |
    |   even if the dealer also busts (therefore Blackjack favors the dealer).                                      |
    |   If both the player and the dealer have the same point value, it is called a "push",                         |
    |   and neither player nor dealer wins the hand. Each player has an independent game with the dealer,           |
    |   so it is possible for the dealer to lose to one player, but still beat the other players in the same round. |
    |                                                                                                               |
    +---------------------------------------------------------------------------------------------------------------+
    """)
        user_answer_input = input('Print (O)Ok to go back: ').lower()
        if user_answer_input == 'o':
            Main()
            break
        else:
            print('Input error! Try again')
            time.sleep(0.5)
            os.system('clear')


def game_core():
    """"
    Run user_core function. Nothing return.
    """
    user_core()


def dealer_core():
    """
    Dealer settings. Nothing return.
    """
    dealer_cards = []
    dealer_score = 0
    while True:
        dealer_cards.append(CARDS_NAMES[random.randrange(0, len(CARDS_NAMES))])
        for card in dealer_cards:
            dealer_score = dealer_score + CARDS_SCORE[card]
            print(
                f'Dealer cards is: {dealer_cards}. Dealer total score is: {dealer_score}')
        if dealer_score < 21:
            continue
        elif dealer_score == 21:
            print(f'Dealer win! His score is: {dealer_score}')
            restart_game()
            break
        elif dealer_score > 21:
            print(f'Dealer lose! His score is: {dealer_score}')
            restart_game()
            break
        break


def user_core():
    """
    User settings. Nothing return.
    """
    user_cards = []
    user_score = 0
    while True:
        user_cards.append(CARDS_NAMES[random.randrange(0, len(CARDS_NAMES))])
        for card in user_cards:
            user_score = user_score + CARDS_SCORE[card]
        if user_score < 21:
            user_answer_input = input(
                f'Your cards is: {user_cards}. Total score is: {user_score}. Do you want (H)Hit or (S)Stay?: ').lower()
            if user_answer_input == 'h':
                continue
            elif user_answer_input == 's':
                dealer_core()
                pass
            else:
                print('Incorrect input! Try again!')
        elif user_score == 21:
            print(f'You win! your score is: {user_score}')
            restart_game()
            break
        elif user_score > 21:
            print(f'You lose! Your score is: {user_score}')
            restart_game()
            break
        break


def restart_game():
    """
    Restart the game. Nothing return.
    """
    while True:
        user_answer_input = input(
            'Do you want to play again? (Y)Yes or (N)No?: ').lower()
        if user_answer_input == 'y':
            Main()
        elif user_answer_input == 'n':
            print('Ok. Goodbuy!')
            break
        else:
            print('Incorrect input! Try again!')
        break


Main()
