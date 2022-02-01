#import random is used in every program here so we write it into the top so we don't have to write it again and again.
 
import random

# 52 Display a random integer between 1 and 100 inclusive.

# num = random.randint(0,100)
# print(num,"is a number between 1 and 100")


# 53 Display a random fruit from a list of five fruits.

# fruit = random.choice(["banana","apple","guvava","grapes","pineapple" ])
# print(fruit,"is good for health.")

# 54 Randomly choose either heads or tails(H or T). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message "You Win", otherwise display "Bas luck". At the end, tell the user if the computer selected heads or tails.

# user_choice = input("Choose H for Head and T for Tails :")
# random_choice = random.choice(["H","T"])
# if user_choice == random_choice:
#     print("You Win!")
# else:
#     print("You Lose!")



# 55 Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly,display the message "Well done", otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display "Correct", otherwise display "You lose"

# num = random.randint(1,5)
# guess = int(input("Enter a number: "))
# if guess == num:
#     print("Well done")
# elif guess > num:
#     print("Too high!")
#     guess = int(input("Guess again :"))
#     if guess == num:
#         print("Correct")
#     else:
#         print("You lose")
# elif guess < num:
#     print("Too low")
#     guess = int(input("Guess again :"))
#     if guess == num:
#         print("Correct")
#     else:
#         print("You lose")

# 56 Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.

# num = random.randint(1,10)
# correct = False
# while correct == False:
#     guess = int(input("Enter a number :"))
#     if guess == num:
#         correct = True



# 57 Update program 56 so that it tells the user id they are too high or too low before they pick again.

# num = random.randint(1,10)
# correct = False
# while correct == False:
#     guess = int(input("Enter a number :"))
#     if guess == num:
#         correct = True
#     elif guess > num:
#         print("Too high")
#     else:
#         print("Too low")


# 58 Make a math quiz that asks five question by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five.

# count = 0
# for i in range(1,6):
#     num1 = random.randint(10,20)
#     num2 = random.randint(10,100)
#     answer = num1 + num2
#     print( num1, "+", num2, "=")
#     ans = int(input("Enter the answer :"))
#     print()
#     if ans == answer:
#         count = count + 1
# print("You scored :", count, "out of 5" )


# 59 Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say "Well done", otherwise display a witty answer which involves the correct colour, e.g. "I bet you are GREEN with envy" or "You are probably feeling BLUE right now". Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly.

# color = random.choice(["red","blue","green","white","pink"])
# print("Select from red,blue,green,white or pink")
# tryagain = True
# while tryagain == True:
#     theirchoice = input("Enter a color :")
#     theirchoice = theirchoice.lower()
#     if color == theirchoice:
#         print("Well done")
#     else:
#         if color == "red":
#             print("I bet you are seeing RED right now !")
#         elif color == "blue":
#             print("Don't feel BLUE :")
#         elif color == "green":
#             print("I bet you are GREEN with envy right now.")
#         elif color == "white":
#             print("Are you WHITE as a sheet, as you didn't guess correctly?")
#         elif color == "pink":
#             print("Shame you are not feeling in the pink.")