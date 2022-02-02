


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

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

elif userchoice == "rock" and computerchoice == "paper":
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




