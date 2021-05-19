import random
from game_data import data
from art import logo1
import os

def contestant_selection(data):
    first_competitor = random.choice(data)
    return first_competitor


def contest(competitor_one, competitor_two):
    from art import logo2
    print(logo1)
    print(f"Compare A: {competitor_one['name']}, {competitor_one['description']}, from {competitor_one['country']}")
#    print(">>>  Vs  <<<")
    print(logo2)
    print(f"Against B: {competitor_two['name']}, {competitor_two['description']}, from {competitor_two['country']}")
    print("Who has more followers? Type 'A' or 'B'")


def followers_comparison(competitor_one, competitor_two):
    if competitor_one['follower_count'] > competitor_two['follower_count']:
        followers_winner = competitor_one
    else:
        followers_winner = competitor_two
    return followers_winner


def guess_verification(winner, first_contestant, second_contestant):
    print(f"The followers winner is: {winner['name']}")
    choice = input("Who has more followers?: ").lower()
    if choice == 'a':
        player_choice = first_contestant
    else:
        player_choice = second_contestant
    return player_choice


def higher_or_lower(first_contestant, second_contestant, consecutives):
    print(f">>> Your streak is the: {consecutives}")
    os.system('clear')    
    # Print participants and 'vs' logo
    contest(first_contestant, second_contestant)
    print(f"Your streak is : {consecutives}")
    # Based in contestants compare their followers and return the contestant with the higher number
    winner = followers_comparison(first_contestant, second_contestant)
    player_choice = guess_verification(winner, first_contestant, second_contestant)    
    if winner == player_choice:
        first_competitor = player_choice
        second_competitor = contestant_selection(data)
        return higher_or_lower(first_competitor, second_competitor, consecutives + 1)
    else:
        print(f">>> Im sorry. You lose. Your streak was: {consecutives}")
        return None

    
while True:
    first_participant = contestant_selection(data)
    second_participant = contestant_selection(data)
    if (first_participant == second_participant):
        continue
    else:
        break

higher_or_lower(first_participant, second_participant, 0)