# SNAKE,WATER,GUN GAME
'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.randint(-1,1)
youstr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:'Snake',-1: 'water',0:'Gun'}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("it's a draw")
else:
    if(computer == -1 and you==1):
       print("you Win!")
    elif(computer == -1 and you ==0):
       print("You Lose!")
  
    elif(computer == 1 and you ==0):
        print("You Win!")
    elif(computer == 1 and you ==-1):
        print("You Lose!")
    
    elif(computer == 0 and you ==1):
        print("You Lose!")
    elif(computer == 0 and you ==-1):
        print("You Win!")

    else:
      print("something went wrong")
     
      

     
     
     
