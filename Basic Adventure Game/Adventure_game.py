# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:39:58 2022

@author: user
"""

name = input("Enter your name: ")
print("Welcome" , name , "to this adventure!!")

answer = input("You are on a dirt road. You have an option to go left or right.Which way would you like to go??").lower()
if answer == "left":
  answer = input("You came across a river . You can walk around or swim. Type walk or swim: ")
  
  if answer == "walk":
     print("You walked for many miles and ran out of water and you lost the game.")
  elif answer == "swim":
     print("You swam across and were eaten by an alligator")
  else:
      print("Not a valid option")

elif answer == "right":
   answer = input("You came across a bridge. It looks wobbly , would you like to cross it or head back . Type cross or back: ").lower()
   
   if answer == "cross":
       print("You fell down of the brigde and you lost the game")
   elif answer == "back":
       print("You won the game")
   else:
      print("Not a valid option")
else:
    print("Not a valid option")