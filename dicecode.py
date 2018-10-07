import random                                   #to take random number
guesses=4                                       #No of chances to be given
win=False                                       #initial condition
game_start = input("*************LETSSSS BEGIN THE GAME******************")
name=str(input("PLAYER NAME-->"))
print("HELLO",name,"I HOPE YOU HAD A GREAT DAY")
print("-------------------- LETS START THE GAME!---------------------")
die1=random.randint(1,7)                        #dice1 random input
die2=random.randint(1,7)                        #dice2 random input
total=die1+die2                                 #adding inputs od dice1 and dice2
try: 
 while guesses>0:                               #condition of chances
  guess=int(input("SO QUICKLY GUESS A NUMBER IN MIND AND ENTER IT--->"))
  guesses=guesses-1                             #decrement number of chances
  if guess>total:
        print("^HINT^-->guessed number is high," ,guesses, "guesses are remaining")     #hint
  elif guess<total:
        print("^HINT^-->guessed number is low",guesses,"guesses are remaining")         #hint
  else:
        print("*_*_*_*_*_*_*CONGRATULATIONS YOU WIN THE GAME*_*_*_*_*_*_*_*")
        win=True                                                                        #condition becomes true
        guesses=0
except  ValueError as e :
 print(e)        

if win==False:                                                                          #check condition and throw result
 print("Oopss, SORRY :( , Your guesses werer incorrect , the no is--->",total)
