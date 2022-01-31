#45 Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and print the message "The total is ...[total]", Stop the loop when the total is over 50.

# total = 0
# while total <= 50:
#     num = int(input("Enter a number : "))
#     total = total + num
#     print("The total is...",total)


#46 Ask the user to enter a number, Keep asking until they enter a value over 5 and then display the message "The last number you entered was a [ number ]" and stop the program.

# num = int(input("Enter a number :"))
# while num < 5:
#     num = int(input("Enter a number : "))
# else:
#     print("The last number you entered is :",num)


#47 Ask the user to enter a number and then enter another number. Add these two number together and then ask if they want to add another number. If they enter "y", ask them to enter another number and keep adding numbers untill they do not answer "n". Once the loop has stopped, display the total.

# Option 1
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number: "))
# total = num1+num2
# choice = input("If you want to add another number write 'y' and if not write 'n' (y/n):")
# while choice == "y":
#         num3 = int(input("Enter a number you want to add :"))
#         total = total + num3
#         choice = input("If you want to add another number write 'y' and if not write 'n' (y/n):")
# else:
#     print("The total is :",total)

# Option 2

# num1 = int(input("Enter a number :"))
# total = num1
# again = "y"
# while again == "y":
#     num2 = int(input("Enter another number :"))
#     total = total + num2
#     again = input("Do you want to add another number?(y/n) :")
# print("The total is",total)


#48 Ask for the name of somebody the user wants to invite to a party. After this, display the message "[name] has been invited " and add 1 to count. Then ask if they want to invite somebody else. Keep repeating this untill they no longer want to invite anyone else to the party and display how many people they have coming to the party.

# again = "y"
# count = 0
# while again == "y":
#     name = input("Enter a name of somebody you want to invite :")
#     print(name, "has been invited")
#     count = count +1
#     again = input("Do you want to invite somebody else(y/n) :")
# print("You have", count, "people coming to your party.")


#49 Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compunum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same values as compnum, display the message "Well done, you took [count] attempts."

# compnum = 50
# guess = int(input("Can you guess the number I am thinking about :"))
# count = 1
# while guess != compnum:
#     if guess < compnum:
#         print("Too low !")
#     else:
#         print("Too high !")
#     count = count + 1
#     guess = int(input("Have another guess :"))
# print("Well done, you took", count, "attempts")


#50 Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message "Too low" and ask them to try again. If they enter a value above 20, display the message "Too high" and ask them to try again. Keep repeating this untill they enter a value that is between 10 and 20 and then display the message "Thank You !"

# num = 15
# guess = int(input("Enter a number between 10 and 20 :"))
# while guess != 15:
#     if guess > num:
#         print("Too high !")
#     else:
#         print("Too low !")
#     guess = int(input("Enter your another guess :"))
# print("Thank you !")

#51 Using the song "10 green bottles", display the lines "There are [num] green bottles hanging on the wall, and if 1 green bottle should  accidentally fall", Then ask the question "how many green bottles will be hanging on the wall ?" If the user answer correctly, display the message "There will be [num] green bottles hanging on the wall", If they answer incorrectly,display the message "No, try again" until they get it right. When the number of green bottles gets down to 0. display the message "There are no more green bottles hanging on the wall"

# num = 10
# while num>0:
#     print("There are", num, "green bottles hanging on the wall ")
#     print(num, "green bottles haniging on the wall .")
#     print("And if 1 green bottle should accidently fall,")
#     num = num - 1
#     answer = int(input("How many green bottles will be hanging on the wall :"))
#     if answer == num:
#         print("There will be", num, "green bottles hanging on the wall ")
#     else:
#         while answer != num:
#             answer= int(input("No, try agin :"))
# print("There are no more green bottles hanging on the wall.")

