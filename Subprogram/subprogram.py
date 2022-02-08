# 118 Define a subprogram that will ask the user to enter a number and save it as the variable "num". Define another subprogram that will use "num" and count from 1 to that number.


# def ask_value():
#     num = int(input("Enter a number : "))
#     return num
# def count(num):
#     n = 1
#     while n<= num:
#         print(n)
#         n = n + 1
# def main():
#     num = ask_value
#     count(num)

# main()
    

# 119 Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two values and store it in a variable called "comp_num".
# Define another subprogram that will give the instruction "I am thinking of a number.." and then ask the user to guess the number they are thinking of.
# Defined a third subprogram that will check to see if the comp_num is the same as the user's guess. If it is,  it should display the message "Correct, you win", otherwise it should keep looping, telling the user if they are too low or too high and asking them to guess again until they guess correctly.

# import random

# def pick_num():
#     low = int(input("Enter the bottom of the range :"))
#     high = int(input("Enter the top of the range :"))
#     comp_num = random.randint(low,high)
#     return comp_num

# def first_guess():
#     print("I am thinking of a number :")
#     guess = int(input("What am I thinking of :"))
#     return guess

# def check_answer(comp_num,guess):
#     try_again = True
#     while try_again == True:
#         if comp_num == guess:
#             print("Congrats, you win.")
#             try_again = False
#         elif comp_num > guess:
#             guess = int(input("Too low, try again :"))
#         else:
#             guess = int(input("Too high, try again :"))
    
# def main():
#     comp_num = pick_num()
#     guess = first_guess()
#     check_answer(comp_num,guess)

# main()


# 120 Display the following menu to the user:
#1) Addition
#2) Subtraction
# Enter 1 or 2
# If they enter a 1, should run a subprogram that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user's answer and the correct answer.
# If they entered 2 as their selection on the menu. it should run the program that will generate one number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have to worry about negative answers. Return both the user's answer and the correct answer.
# Create another subprogram that will check if the user's answer matches the actual answer. If it does, display "Correct", otherwise display a message that will say "Incorrect, the answer is" and display the real answer.

#If they do not select a relevent option on the first menu you should display a suitable message.

# import random

# def additon():
#     num1 = random.randint(5,20)
#     num2 = random.randint(5,20)
#     print(num1, "+", num2, "=" )
#     user_answer = int(input("Your answer :"))
#     actual_answer = num1 + num2
#     answers = (user_answer,actual_answer)
#     return answers

# def subtracton():
#     num3 = random.randint(5,20)
#     num4 = random.randint(5,20)
#     print(num3, "-", num4, "=" )
#     user_answer = int(input("Your answer :"))
#     actual_answer = num3 - num4
#     answers = (user_answer,actual_answer)
#     return answers

# def check_answer(user_answer,actual_answer):
#     if user_answer == actual_answer:
#         print("Correct")
#     else:
#         print("Incorrect, the actual answer is", actual_answer)

# def main():
#     print("1) Addition\n2) Subtraction ")
#     selection = int(input("Choose an option :"))
#     if selection == 1:
#         user_answer, actual_answer = additon() #user_answer and actual answer are variables but we have to wirte it at it is because when the code is runned by the user check answer function also run which only comapare that variable which we assaigned to them so we write it in the way that it will fullfilling all the conditions.
#         check_answer(user_answer,actual_answer)
#     elif selection == 2:
#           user_answer, actual_answer = subtracton()
#           check_answer(user_answer,actual_answer)
#     else:
#         print("Incorrect selection")

# main()  




# 121 Create a program that will allow the user to easily manage a list of names. You should display a menu that will allow them to add a name to the list, change a name in the list, delete a name from the list or view all the names in the list. There should also be a menu option to allow the user to end the program. If they select an option that is not relevent, then it should display the suitable message. After they have made a selection to either add a name, change a name, delete a name or view all the names, they should see the menu again without having a restart the program. The program should be made as easy to use as possible.


# def add_name():
#     name = input("Enter a new name :")
#     names.append(name)
#     return name

# def change_name():
#     num = 0
#     for x in names:
#         print(num,x)
#     select_num = int(input("Enter the number of the name you want to change :"))
#     name = input("Enter new name :")
#     names[select_num] = name
#     return names

# def delete_name():
#     num = 0
#     for x in names:
#         print(num,x)
#         num = num + 1
#     select_num = int(input("Enter the number of the name you want to delete :"))
#     del names[select_num]
#     return names

# def view_names():
#     for x in names:
#         print(x)
#     print()

# def main():
#     again = "y"
#     while again == "y":
#         print("1) Add a name ")
#         print("2) Change a name")
#         print("3) Delete a name")
#         print("4) View names")
#         print("5) Quit")
#         selection = int(input("What do you want to do ?\nChoose any option :"))
#         if selection == 1: 
#             names = add_name()
#         if selection == 2:
#             names = change_name() 
#         if selection == 3:
#             names = delete_name() 
#         if selection == 4:
#             names = view_names() 
#         if selection == 5:
#             again = "n" 
#         else:
#             print("Incorrect option :") 
#         data = (names,again)
# names = []
# main()



# 122 Create the following menu:

# 1) Add to file
# 2) View all records
# 3) Quit program

# Enter the number of your selection:

# If they user selects 1, allow them to add to a file called Salaries.csv file, which will store their name and salary. If they select 2 it should display all records in the Salaries.csv file. If they select3 it should stop the program. If they select an incorrect option they should keep returning to the menu until they select option 3.


# def addfile():
#     file = open("Salaries.csv","a")
#     name = input("Enter your name :")
#     salary = int(input("Enter your salary :"))
#     newrecord = name + "," + str(salary) + "," + "\n"
#     file.write(str(newrecord))
#     file.close()

# def viewrecords():
#     file = open("Salaries.csv","r")
#     for row in file:
#         print(row)
#     file.close()

# def main():
#     print("1) Add to file\n2) View all records\n3) Quit program")
#     selection = int(input("Enter the number of your selection :"))
#     try_again = True
#     while try_again == True:
#         if selection == 1:
#             addfile()
#             try_again = False
#         elif selection == 2:
#             viewrecords()
#             try_again = False
#         elif selection == 3:
#             try_again = False
#         else:
#             print("Incorrect option!")

# main()

# 123 In Python, it is not technically possible to directly delete a record from a .csv file. Instead you need to save the file to temporary list in Python, make the changes to the list and then overwrite the orignal file with the temprorary list.
# Change the previous program to allow you to do this. You menu should now look like this:

# 1) Add to file
# 2) View all records
# 3) Delete a record
# 4) Quit program

# Enter the number of your selection:

# def addfile():
#     file = open("Salaries.csv","a")
#     name = input("Enter your name :")
#     salary = int(input("Enter your salary :"))
#     newrecord = name + "," + str(salary) + "," + "\n"
#     file.write(str(newrecord))
#     file.close()

# def viewrecords():
#     file = open("Salaries.csv","r")
#     for row in file:
#         print(row)
#     file.close()

# def deleterecord():
#     file = open("Salaries.csv","r")
#     x = 0
#     tmplist = []
#     for row in file:
#         tmplist.append(row)
#     file.close()
#     for row in tmplist:
#         print(x,row)
#         x = x+1
#     rowtodelete = int(input("Enter the row number you want to delete :"))
#     del tmplist[rowtodelete]
#     file = open("Salaries.csv","w")
#     for row in tmplist:
#         file.write(row)
#     file.close()

# def main():
#     print("1) Add to file\n2) View all records\n3) Delete a recoard\n4) Quit program")
#     selection = int(input("Enter the number of your selection :"))
#     try_again = True
#     while try_again == True:
#         if selection == 1:
#             addfile()
#             try_again = False
#         elif selection == 2:
#             viewrecords()
#         elif selection == 3:
#             deleterecord()
#             try_again = False
#         elif selection == 4:
#             try_again = False
#         else:
#             print("Incorrect option!")

# main()
