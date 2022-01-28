#12 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# if a>b:
    # print("The value of a is " , b, "and the value of b is",a)
# else:
    # print("The value of a is ", a, "and the value of b is", b)



#13 Ask the user to enter a number that is undr 20. If they enter a number that is 20 or more, display the message "Too high", otherwise display "Thank you"

# num = int(input("Enter a number under 20 :"))
# if num>=20:
    # print("Too High")
# else:
    # print("Thank You !")


#14 Ask the user to enter a number between 10 and 20 . If they enter a number within this range, display the message "Thank You", otherwise display the message "Incorrect answer".

# num = int(input("Enter a number between 10 and 20 :"))
# if num>=10 and num<=20:
    # print("Thank You !")
# else:
    # print("Incorrect answer!")



#15 Ask the user to enter their favourite color. If they enter "red ", "RED" or "Red" display the message "I like red too", otherwise display the message "I don't like [color], I prefer red".


# color = input("Enter your favourite color : ")
# if color == "RED" or color == "Red" or color == "red":
    # print("I like red too")
# else:
    # print("I don't like", color,", I prefer red")


#16 Ask the user if it is raining and convert their ansewer to lower case so it doesnt't matter what case they type it in. If they answer "Yes" ask if it is windy. If they answer "yes" to this second question, display the answer "It is too windy for an umberella", otherwise display the message "Take an umberella", If they did not answer yes to the first question, display the answer "Enjoy your day"

raining = input("Is it raining today :")
raining = str.lower(raining)
 #for convert the answer into lower case
# if raining == "yes":
#     windy = input("Is it windy? ")
#     windy = str.lower(windy)
#     if windy == "yes":
#         print("It is too windy for an umberella")
#     else:
#         print("Take an umberella")
# else:
#     print("Enjoy your day")

#17 Ask the user's age. If they are 18 or over,display the message "You can vote", if they are aged 17, display the message "You can learn to drive", if they are 16, display the message "You can buy a lottery ticket", if they are under 16, display the message "You can go Trick-or-Treating"

# age = int(input("Enter your age :"))
# if age >= 18:
#     print("You can vote")
#     if age == 17:
#         print("You can learn to drive")
#         if age == 16:
#             print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

#18 Ask the user to enter a number, If it is under 10, display the message "Too low", if their number is between 10 and 20, display "Correct", otherwise display "Too high".

# num = int(input("Enter a number :"))
# if num <= 10:
#     print("Too low")
#     if num >= 10 and num <= 20:
#         print("Correct")
# else:
#     print("Too high")


#19 Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

# num = int(input("Choose a number : 1 , 2 , 3 : "))
# if num == 1:
#     print("Thank You!")
#     if num == 2: 
#         print("Well done !")
#         if num == 3:
#             print("Correct !")
# else:
#     print("Error message !!!")




