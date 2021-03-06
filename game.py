

# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#



#PLAYER NAME
# this is the "game.py" file...

from gettext import install
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

player_name = os.getenv("PLAYER_NAME", default="Player One")

print("Player Name is:", os.environ.get('PLAYER_NAME'))





#USER INPUT 
userchoice = input("Choose one: 'rock', 'paper', 'scissors'!")

print("USER CHOSE:", userchoice)

#VALIDATE USER INPUT 
validchoices = ['rock','ROCK','Rock','PAPER','paper','Paper','SCISSORS','scissors','Scissors']

if userchoice not in validchoices:
    print("Oops! You did not enter 'rock', 'paper', or 'scissors'.")
    print(exit)



#COMPUTER SIMULATION 
#followed this part in class, thank you Professor Rossetti! 
import random
options = ["rock","paper","scissors"]
computerchoice = random.choice(options)
print("COMPUTER CHOSE:", computerchoice)



#DETERMINING THE WINNER 
if userchoice == computerchoice:
    print("It's a tie game!")

if userchoice == "rock" and computerchoice == "paper":
    print("Sorry! You Lost")
elif userchoice == "rock" and computerchoice == "scissors":
    print("Yay! You won!")
elif userchoice == "paper" and computerchoice == "rock":
    print("Yay! You won!")
elif userchoice == "paper" and computerchoice == "scissors":
    print("Sorry! You Lost.")
elif userchoice == "scissors" and computerchoice == "rock":
    print("Sorry! You Lost.")
elif userchoice == "scissors" and computerchoice == "paper":
    print ("Yay! You won!")

#FINAL MESSAGE 
print("Thanks For Playing! :D")



