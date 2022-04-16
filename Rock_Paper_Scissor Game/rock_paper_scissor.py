# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:12:37 2022

@author: user
"""

import random
import sys

user_wins = 0
computer_wins = 0
options = ["rock" , "paper" , "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_input == 'q':
        break #come out of while loop

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0 , paper:1 , scissor:2
    
    computer_pick = options[random_number]
    print("Computer Picked" , computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You win")
        user_wins += 1
      
    elif user_input == "scissor" and computer_pick == "paper":
        print("You win")
        user_wins += 1
      
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1
    else:
        print("You lost:(")
        computer_wins += 1 
        print("Computer Wins!!:)")

print("You won", user_wins , "times")
print("Computer wins ",computer_wins , "times" )
print("GoodBye!!")