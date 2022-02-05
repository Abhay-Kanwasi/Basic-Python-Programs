# 105 Write a new file called "Number.txt". Add five numbers to the document which are stored on the same line and only seperated by a comma. Once you have run the program, look in the location where your program is stored and you should see that file has been created. The easiest way to view the contents of the new text file on a windows system is to read it using Notepad.

# file = open("Numbers.txt","w")
# file.write("4, ")
# file.write("9, ")
# file.write("1, ")
# file.write("7, ")
# file.write("5, ")
# file.close()


# 106 Create a new file called "Names.txt". Add five names to the document, which are stored on seperate lines. Once you have run the program, look in the location where your program is stored and check that the file has been created properly.

# file = open("Names.txt","w")
# file.write("Python\n")
# file.write("R\n")
# file.write("Ruby\n")
# file.write("Secrate doc.\n")
# file.write("Software\n")
# file.close()


# 107 Open the Names.txt file and display the data in Python

# file = open("Names.txt","r")
# print(file.read())
# file.close()


# 108 Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file.

# file = open("Names.txt","a")
# file.write("Free Fire\n")
# file.close()
# file = open("Names.txt","r")
# print(file.read())
# file.close()


# 109 Display the following menu to the user :
# 1) Create a new file
# 2) Display the file
# 3) Add a new item to the file Make a selection 1,2 or 3:

# Ask the user to enter 1,2 or 3. If theys select 1, ask the user to enter a school subject and save it to a new file called "Subject.txt". It should overwrite any existing file with a new file. 

# If they select 2, display the contents of the "Subject.txt" file.

# If they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.

# Run the program several times to test the options.

# print("1) Create a new file. ")
# print("2) Display the file. ")
# print("3) Add a new item to the file. ")
# option = int(input("Choose any option : "))
# if option == 1:
#     sub = input("Enter a school sub :")
#     file = open("Subject.txt","a")
#     file.write(sub)
#     file.close()
# elif option == 2:
#     file = open("Subject.txt","r")
#     print(file.read())
    # file.close()
# elif option == 3:
#     sub1 = input("Enter a new subject :")
#     file = open("Subject.txt","a")
#     file.write(sub1)
#     file.close()
#     file = open("Subject.txt","r")
#     print(file.read())
# else:
#     print("Invalid Option!")



# 110 Using the Names.txt file you created earlier, display the list of names in Python. Ask the user to type in one of the names and then save all the names except the one they entered into a new file called Names2.txt.

file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
ask = input("Choose one of these names :")
ask = ask + "\n"
for row in file:
    if row != ask:
        file = open("Names2.txt","a")
        new = row
        file.write(new)
        file.close()
file.close()
