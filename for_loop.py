#35 Ask the user to enter their name and then display their name three times.


# name = input("Enter your name")
# for i in range(0,3):
#     print(name)


#36 Alter program 35 so that it will ask the user to enter the name and a number and then display their name that number of times

# name = input("Enter your name : ")
# num = int(input("Enter a number: "))
# for i in range(0,num):
#     print(name)


#37 Ask the user to enter their name and display each letter in their name on a seperate line.

# name = input("Enter your name : ")
# for i in name:
#     print(i)


#38 Change program 37 to also ask for a number. Display their name(one letter at a time on a each line) and repeat this for the number of times they entered

# num = int(input("Enter a number :"))
# for i in range(0,num):
#     name = input("Enter your name :")
#     for i in name:
#         print(i)


#39 Ask the user to enter a number between 1 and 12 and then diplay the times table for a number.

# num = int(input("Enter a number between 1 and 12 : "))
# for i in range(1, 13):
#     answer = i*num
#     print(i, "x", num, "=", answer)


#40 Ask for a number below 50 and then count down from 50 to that number, making sure you show the number in the output.

# num = int(input("Enter a number below 50 : "))
# for i in range (50,num-1,-1):
#     print(i)


#41 Ask the user to enter their name and a number is less than 10, then display their name that number of times; otherwise display the message "Too high" three times.

# name = input("Enter a name :")
# num = int(input("Enter a number :"))
# if num<10:
#     for i in range(0,num):
#         print(name)
# else:
#     for i in range(0,3):
#         print("Too high !!!")

#42 Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included,don't add it to the total. After they have entered all five numbers, display the total.

# total = 0
# for i in range(0,5):
#     num = int(input("Enter a number :"))
#     ans = input("Do you want this number included/ (y/n) ")
#     if ans == "y":
#         total = total + num
# print(total)

#43 Ask which direction the user wants to count(up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message "I don't understand".

# dir = input("Choose the direction you want to count(up/down) : ")
# if dir == "up":
#     top = int(input("Enter the top number :"))
#     for i in range(1,top+1):
#         print(i)
# if dir == "down":
#     dowm = int(input("Enter a number below 20 :"))
#     for i in range(20,dowm-1,-1):
#         print(i)
# else:
#     print("I don't understand!")

#44 Ask how many people the user wants to invite to a party. If they enter a number below 10. ask for the names and after each name display "[name]has been invited". If they enter a number which is 10 or higher, display the message "Too many people"

# num = int(input("How many people you want to invite : "))
# if num < 10:
#     for i in range(0,num):
#       name = input("Enter name :")
#       print(name,"has been invited")
# else:
#     print("Too many peoples !!")

