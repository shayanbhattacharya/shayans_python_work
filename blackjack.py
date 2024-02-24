#Importing modules needed to randomise the card dealing and detect what sort of OS the user has
import random
import os
import platform

#Creating a function to clear the console, regardles of whther you use a mac or PC
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Creating a function called 'deal()' to generate a random card. 11 is the ace.
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Creating a function to take the list of cards as input and return score
#Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Establishing the rules of blackjack with a function called compare
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

#Deal the user and computer 2 cards each using deal()
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())
    
    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
             user_cards.append(deal())
            else:
               is_game_over = True

  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal())
      computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#HAsk the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
