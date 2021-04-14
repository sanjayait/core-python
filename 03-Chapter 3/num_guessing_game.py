# win_num=65
# guess=1
# num=int(input("guess a number b\\t 1 - 100 : "))
# game_over=False
# while not game_over:
#     if num==win_num:
#         print(f" You win! and You guessed {guess} times")
#         game_over=True
#     else:
#         if num <win_num:
#             print("too low")
#             guess +=1
#             num=int(input("Guess again : "))
#         else:
#             print("too high") 
#             guess +=1
#             num= int(input("Guess again : "))  

# DRY principle of coding: 
import random    
win_num= random.randint(1,100)
guess=1
num=int(input("Guess a number between 1-100 : "))
gameover=False
while not gameover:
    if num==win_num:
        print(f"YOU WIN ! and You guessed {guess} times")
        gameover=True
    else:
        if num<win_num:
            print("guessed low") 
        else:
            print("guessed high")       
        guess +=1
        num= int(input("Guess again : "))
    # DRY= Don't repeat yourself