# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# USER'S TURN
welcome_msg = int(input('Welcome to Blackjack! How many players? '))
# player_1 = input("What is player 1's name? ")
# player = input("What is player 2's name? ")
players_scores = {}
for player in range(welcome_msg):
  player = input("What is player {}'s name? ".format(player + 1))
  players_scores[player] = 3
#print(players_scores)

players_hands = {}
for player in players_scores:
  user_hand = draw_starting_hand("{}'S".format(player.upper()))
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
  players_hands[player] = user_hand
  print_end_turn_status(user_hand)
# print(players_hands)

# DEALER'S TURN
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  dealer_hand = dealer_hand + draw_card()
print_end_turn_status(dealer_hand)
# for player,value in players_hands.items():
# new_round = input('Do you want to play another hand (y/n)? ')  
# GAME RESULT
print_end_game_status(players_scores, players_hands, dealer_hand)

while continue_game(players_scores):
    new_round = input('Do you want to play another hand (y/n)? ')
    if new_round == 'n':
      break
    elif new_round == 'y':
      for player in players_scores:
        user_hand = draw_starting_hand("{}'S".format(player.upper()))
        should_hit = 'y'
        while user_hand < 21:
          should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
          if should_hit == 'n':
            break
          elif should_hit != 'y':
            print("Sorry I didn't get that.")
          else:
            user_hand = user_hand + draw_card()
        players_hands[player] = user_hand
        print_end_turn_status(user_hand)
    # print(players_hands)

# DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
      print("Dealer has {}.".format(dealer_hand))
      dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)
    print_end_game_status(players_scores, players_hands, dealer_hand)


















