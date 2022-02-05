# We have to import .csv file every time so we import it here So, use it in every code.

import csv

# # 111 Create .csv file that will store the data of some books, book authors and the year book was released.

# file = open("Books.csv","w")
# newRecord = "Books, Authors, Year\n"
# file.write(str(newRecord))
# newRecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
# file.write(str(newRecord))
# newRecord = "A Brief History of Time, Stephan Hawking, 1988\n"
# file.write(str(newRecord))
# newRecord = "The Great Gatsby,F.Scott Fitzgerald, 1922\n"
# file.write(str(newRecord))
# newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# file.write(str(newRecord))
# newRecord = "Pride and Prejudice, Jane Austen, 1813\n"
# file.write(str(newRecord))
# file.close()



# 112 Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. Display each row of the .csv file on a seperate line.

# file = open("Books.csv","a")
# book_name = input("Enter book name :")
# author_name = input("Enter author name :")
# year_name = input("Enter the year  :")
# newRecord = book_name + "," + author_name + "," + year_name + "\n"
# file.write(str(newRecord))
# file.close()


# 113 Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many. After alll the data has been added, ask for an author and display all the books in the list by that author. If there are no books by that author in the list, display a  suitable message.


# file = open("Books.csv","a")
# records = int(input("How many records you want to add :"))
# for x in range(0,records):
#    book_name = input("Enter book name :")
#    author_name = input("Enter author name :")
#    year_name = input("Enter the year  :")
#    newRecord = book_name + "," + author_name + "," + year_name + "\n"
#    file.write(str(newRecord))
# file.close()

# search = input("Enter the author's name :")
# file = open("Books.csv","r")
# count = 0
# for row in file:
#     if search in str(row):
#         print(row)
#         count = count + 1
# if count == 0:
#     print("There are no books by that author in this list")
# file.close()



# 114 Using the Books.csv file, ask the user to enter a starting year and an end year. Display all books released between those two years.

# start = int(input("Enter the starting year :"))
# end = int(input("Enter the last year :"))

# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)

# x = 0
# for row in tmp:
#     if int(tmp[x] [2]) >= start and int(tmp[x] [2]) <= end:
#         print(tmp[x])
#     x = x + 1


# 115 Using the Books.csv file, display the data in the file along with the row number of each.

# file = open("Books.csv","r")
# x = 0
# for row in file:
#     display = "Row :" + str(x) + " - " + row
#     print(display)
#     x=x+1

# 116 Import the data from the Books.csv file into a list. Display the list to the user. Ask them to select which row from the list they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it. Write a data back to the orignal .csv file, overwriting the existing data with the amended data.

# #import data
# file = list(csv.reader(open("Books.csv")))
# Booklist = []
# for row in file:
#     Booklist.append(row)

# #display to the user
# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x=x+1
# getrid = int(input("Enter a row number to delete :")) 
# #select which one to delete
# del Booklist[getrid]

# # data wants to change
# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x = x+1
# alter = int(input("Enter a row number to alter : "))
# x = 0
# for row in Booklist[alter]:
#     display = x,Booklist[alter][x]
#     print(display)
#     x=x+1
# part = int(input("Which part do you want to change?"))
# newdata = input("Enter new data :")
# Booklist[alter][part] = newdata
# print(Booklist[alter])

# # Overwritting the previous data
# file = open("Books.csv","w")
# x = 0
# for row in Booklist:
#     newrecord = Booklist[x][0] + ","+ Booklist[x][1] + "," + Booklist[x][2] + "\n"
#     file.write(newrecord)
#     x=x+1
# file.close()


# 117 Create a simple math quiz that will ask the user for their name and then generate two random questions. Store their name, the question they were asked, their answers and their final score in a .csv file. Whenever the program is run it should add to the .csv file and not overwrite anything.

# import random 
# score = 0
# name = input("Enter your name :")
# q1_num1 = random.randint(10,50)
# q1_num2 = random.randint(10,50)
# question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
# ans1 = int(input(question1))
# realans1 = q1_num1 + q1_num2
# if ans1 == realans1:
#     score = score + 1
# q2_num1 = random.randint(10,50)
# q2_num2 = random.randint(10,50)
# question2 = str(q2_num1) + " + " + str(q1_num2) + " = "
# ans2 = int(input(question2))
# realans2 = q2_num1 + q2_num2
# if ans2 == realans2:
#     score = score + 1

# file = open("QuizScore.csv","a")
# newrecord = name + "," + question1+ str(ans1) + "," + question2 + str(ans2) + "," + str(score) + "\n"
# file.write(str(newrecord))

# file.close()

