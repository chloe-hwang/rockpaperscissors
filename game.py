


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
    print("error! Pls input rock, paper, or scissors.")
    
