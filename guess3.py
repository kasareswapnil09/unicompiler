'''
UNIcompiler

(PYTHONVERSE)

TASK-1 (EASY)
                     ******   NUMBER GUESSING     *****
1. Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
2. Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue,and his score gets reduced.
3. The clue can be multiples, divisible, greater or smaller, or a combination of all.

'''

import math
import random


 # taking the limitation to consider between them convt. to guess no.
lower_Number = int(input("Please Enter the Lower Number :"))

Highter_Number = int(input("Please Enter the Higher Number : "))

a = random.randint(lower_Number,Highter_Number)
print("\n\t You've have only",
        round(math.log(Highter_Number - lower_Number + 1,2)),
        "Chances to Guess the Number! \n")


count = 0

while count < math.log(Highter_Number - lower_Number +1 ,2 ):
    count +=1

    Guess = int(input("Please Guess the Number : "))


    if a == Guess:
        print("Congratulation You won!",
            count, "Please try Again! ")

        break
    elif a > Guess:
        print("\nYou Guessed Lower Number! ","You have remaining guessing of step no: ",count)
        count <=1
    elif a < Guess:
        print("\nYou Guessed Higher Number!","You have remaining guessing of step no: ",count)
        count <=1

if count >= math.log(Highter_Number - lower_Number + 1,2):
    print("\n The Your Guessing Number is %d " % a)
    print("\t BETTER LUCK FOR NEXT TIME BUDDY!")
