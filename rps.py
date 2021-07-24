"""
ROCK PAPER SCISSORS

This program is basically user vs. computer in a game of rock paper scissors. It will continue playing until user decides to quit and end the game.

This program is made for fun and experimenting purposes.
"""
import random

def comp_decision(choices):
    comp_final = random.choice(choices)
    return comp_final

def check_user_choice(user_choice, choices):
    if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        return user_choice
    else:
        print("Please enter a valid option next time! Initializing random option...")
        return random.choice(choices)


def point_winner(user_choice, comp_choice):
    message = ''
    user_add = 0
    comp_add = 0
    if (user_choice == comp_choice):
        message = 'TIE'
    elif user_choice == 'rock':
        if comp_choice == 'scissors':
            user_add = 1
            message = "{} beats {}".format(user_choice, comp_choice)
        elif comp_choice == 'paper':
            comp_add = 1
            message = "{} beats {}".format(comp_choice, user_choice)
    elif user_choice == 'paper':
        if comp_choice == 'rock':
            user_add = 1
            message = "{} beats {}".format(user_choice, comp_choice)
        elif comp_choice == 'scissors':
            comp_add = 1
            message = "{} beats {}".format(comp_choice, user_choice)
    elif user_choice == 'scissors':
        if comp_choice == 'paper':
            user_add = 1
            message = "{} beats {}".format(user_choice, comp_choice)
        elif comp_choice == 'rock':
            comp_add = 1
            message = "{} beats {}".format(comp_choice, user_choice)
    return message, user_add, comp_add


def game_winner(user_points, comp_points):
    if user_points > comp_points:
        return "\nCongrats! You won against the computer with a score of {} to {}!".format(user_points, comp_points)
    elif user_points < comp_points:
        return "\nYou Lost! The computer won against you with a score of {} to {}! Try again next time!".format(comp_points, user_points)
    else:
        return "\nYou got tied with the computer with a score of {}. Try to win next time!".format(user_points)


def beginning_design():
    intro = 'Welcome to Rock Paper Scissors'
    number_sign = ''
    for i in range(len(intro)):
        number_sign += '#'
    print("\n{}\n{}\n{}\n".format(number_sign, intro, number_sign))


def game():
    user_points = 0
    comp_points = 0
    choices = ['rock', 'paper', 'scissors']

    beginning_design()
    to_play = input("| Type P to Play |\n| Type Q to Quit |\nYour Input: ").lower()

    while to_play != 'q' and to_play != 'n':
        if to_play != 'p' and to_play != 'y':
            print("\nYou chose a letter that wasn't in the options. Still going to start the game you rule breaker!")
        user_choice = input("\nRock, Paper, or Scissors?: ").lower()
        user_choice = check_user_choice(user_choice, choices)
        comp_choice = comp_decision(choices)

        winner_info = point_winner(user_choice, comp_choice)
        message = winner_info[0].upper()
        user_points += winner_info[1]
        comp_points += winner_info[2]

        print("\n{}\nYou: {}\tComp: {}".format(message, user_points, comp_points))

        to_play = input("\n| Play Again? Y/N |\nYour Input: ").lower()

        if to_play == 'n':
            print(game_winner(user_points, comp_points))
            print("Thank You for playing! Play again soon!")
        elif to_play != 'y':
            print("\nStarting next game... Next time type Y or N only!\n")


game()
    