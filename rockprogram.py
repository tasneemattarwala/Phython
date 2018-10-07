import random                             #importing random input
import sys                                #import system module

computerscore=0                           #initialize values
userscore=0
count = 0

def play():                             #create function        
    global count
  
    while count < 3 :                   #condition
   
        player=input("enter your choice")           #take user input 
        choices={1:"rock",2:"paper",3:"scissors"}
        computer = choices[random.randint(1,3)]     #take computers random input
    
        global computerscore                        #display score
        global userscore
   
        if player == computer:                      #condition for tie
            print("Tie!")
        
            count = count + 1
            play()
        #print(score)               
        elif player == "rock":              
            if computer == "paper":                 #condition for lose                
                print("You lose!")
                computerscore = computerscore + 1
                
           # print(score)
                count = count + 1                   #increment score
                print(computerscore)
                print(userscore)
                play()
            
            #return computerScore
            else:
                print("You win!")                   #condition to win
                userscore = userscore + 1 
                count = count + 1
                print(userscore)
                print(computerscore)
                play()
            
        elif player == "paper":                       #check different conditions
            if computer == "scissors":
                print("You lose!")
                computerscore = computerscore + 1
            #print(score)   
                count = count + 1                        #calculate score
                print(userscore)
                print(computerscore)  
                play()
            
            else:
                print("You win!")                        #check different conditions
                userscore = userscore + 1
            
                count = count + 1
                print(userscore)
                print(computerscore)
                play()
        elif player == "scissors":                        #conditions
            if computer == "rock":
                print("You lose!")
                computerscore = computerscore + 1   
            #print(score)
                count = count + 1
                play()
            
            else:
                print("You win!" )                           #conditions and score
                userscore = userscore + 1 
                count = count + 1
                print(userscore)
                print(computerscore)
                play()
           
            
        else: 
            print("That's not a valid play. Check your spelling!")
            count = count + 1
            play()
    if count == 3 :
        count = 0
        try_again()
    
def try_again():                                        #function for game
    choice=input("would you like to continue? y/n") 
    if choice=="y":                                     #conditions
        return computerscore
        return userscore
        play()
        
    
    elif choice=="n":                                   #conditions
        print("thanks for playing")
        quit()
    else:
        print("try again")
        try_again()
play()
